# -*- coding: utf-8 -*-

from zope.interface import implements

from imio.urban.dataimport.acropole.importer import AcropoleDataImporter
from Florennes.urban.dataimport.interfaces import IFlorennesDataImporter


class FlorennesDataImporter(AcropoleDataImporter):
    """ """

    implements(IFlorennesDataImporter)
