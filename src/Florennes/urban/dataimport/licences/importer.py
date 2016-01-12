# -*- coding: utf-8 -*-

from zope.interface import implements

from Florennes.urban.dataimport.interfaces import IFlorennesDataImporter
from Florennes.urban.dataimport.licences import valuesmapping

from imio.urban.dataimport.acropole.importer import AcropoleDataImporter
from imio.urban.dataimport.acropole.importer import AcropoleValuesMapping


class LicencesImporter(AcropoleDataImporter):
    """ """

    implements(IFlorennesDataImporter)

    def __init__(self, db_name='urb93022ac', table_name='wrkdossier', key_column='WRKDOSSIER_ID', savepoint_length=0):
        super(AcropoleDataImporter, self).__init__(db_name, table_name, key_column, savepoint_length)


class LicencesValuesMapping(AcropoleValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return valuesmapping.VALUES_MAPS.get(mapping_name)
