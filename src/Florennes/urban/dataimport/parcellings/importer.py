# -*- coding: utf-8 -*-

from zope.interface import implements

from Florennes.urban.dataimport.interfaces import IFlorennesDataImporter
from Florennes.urban.dataimport.parcellings import objectsmapping
from Florennes.urban.dataimport.licences import valuesmapping

from imio.urban.dataimport.mapping import ObjectsMapping
from imio.urban.dataimport.mapping import ValuesMapping
from imio.urban.dataimport.MySQL.importer import MySQLDataImporter


class ParcellingsImporter(MySQLDataImporter):
    """ """

    implements(IFlorennesDataImporter)

    def __init__(self, db_name='urb93022ac', table_name='urblot', key_column='URBLOT_ID', savepoint_length=0):
        super(ParcellingsImporter, self).__init__(db_name, table_name, key_column, savepoint_length)


class ParcellingsMapping(ObjectsMapping):
    """ """

    def getObjectsNesting(self):
        return objectsmapping.OBJECTS_NESTING

    def getFieldsMapping(self):
        return objectsmapping.FIELDS_MAPPINGS


class ParcellingsValuesMapping(ValuesMapping):
    """ """

    def getValueMapping(self, mapping_name):
        return valuesmapping.VALUES_MAPS.get(mapping_name)
