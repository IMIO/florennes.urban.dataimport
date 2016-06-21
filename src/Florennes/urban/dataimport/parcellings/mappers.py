# -*- coding: utf-8 -*-

from imio.urban.dataimport.MySQL.mapper import MySQLMapper as Mapper
from imio.urban.dataimport.MySQL.mapper import MultiLinesSecondaryTableMapper

from imio.urban.dataimport.factory import BaseFactory

from Products.CMFPlone.utils import normalizeString

from imio.urban.dataimport.utils import CadastralReference
from imio.urban.dataimport.utils import parse_cadastral_reference

#
# PARCELLINGS
#

# factory


class ParcellingFactory(BaseFactory):
    def getCreationPlace(self, factory_args):
        return self.site.urban.parcellings

    def getPortalType(self, container, **kwargs):
        return 'ParcellingTerm'


class ParcelFactory(BaseFactory):
    def create(self, parcel, container=None, line=None):
        searchview = self.site.restrictedTraverse('searchparcels')

        if parcel is None:
            return None

        #need to trick the search browser view about the args in its request
        parcel_args = parcel.to_dict()
        parcel_args.pop('partie')

        for k, v in parcel_args.iteritems():
            searchview.context.REQUEST[k] = v
        #check if we can find a parcel in the db cadastre with these infos
        found = searchview.findParcel(**parcel_args)
        if not found:
            found = searchview.findParcel(browseoldparcels=True, **parcel_args)

        if len(found) == 1 and parcel.has_same_attribute_values(found[0]):
            parcel_args['divisionCode'] = parcel_args['division']
            parcel_args['isOfficialParcel'] = True
        else:
            self.logError(self, line, 'Too much parcels found or not enough parcels found', {'args': parcel_args, 'search result': len(found)})
            parcel_args['isOfficialParcel'] = False

        parcel_args['id'] = parcel.id
        parcel_args['partie'] = parcel.partie

        return super(ParcelFactory, self).create(parcel_args, container=container)

    def objectAlreadyExists(self, parcel, container):
        if not parcel:
            return
        existing_object = getattr(container, parcel.id, None)
        return existing_object


# mappers
class IdMapper(Mapper):
    def mapId(self, line):
        return normalizeString(self.getData('URBLOT_ID'))


class ParcellingMapper(Mapper):

    def init_query(self, table):
        datasource = self.importer.datasource
        query = datasource.session.query(datasource.get_table(table))
        return query

    def __init__(self, mysql_importer, args):
        super(ParcellingMapper, self).__init__(mysql_importer, args)
        self.table = args['table']
        self.query = self.init_query(self.table)
        prc_lotiss = self.importer.datasource.get_table('prc_lotiss')
        urblot = self.importer.datasource.get_table('urblot')

        self.query = self.query.join(
            prc_lotiss,
            urblot.columns['URBLOT_ID'] == prc_lotiss.columns['PRCL_LOTISID']
        )

    def mapId(self, line):
        return normalizeString(self.getData('URBLOT_ID'))

    def mapLabel(self, line):
        return self.getData('LOT_NUM')

    def mapSubdividername(self, line):
        return self.getData('LOT_NOM')

    def mapAuthorizationdate(self, line):
        return self.getData('LOT_DATE')

    def mapNumberofparcels(self, line):
        return self.getData('LOT_NBLOT')


class ParcelDataMapper(Mapper):

    def map(self, line, **kwargs):

        raw_reference = self.getData('PRCL_PRC')
        reference = parse_cadastral_reference(raw_reference)
        cadastral_ref = CadastralReference(*reference)
        division_map = self.getValueMapping('division_map')
        if cadastral_ref.division:
            cadastral_ref.division = division_map[cadastral_ref.division]
        else:
            cadastral_ref = None
        return cadastral_ref


class ParcelsMapper(MultiLinesSecondaryTableMapper):
    """ """
