# -*- coding: utf-8 -*-

from Florennes.urban.dataimport.parcellings.importer import ParcellingsImporter
from imio.urban.dataimport.browser.adapter import ImporterFromSettingsForm
from imio.urban.dataimport.browser.import_panel import ImporterSettings


class ParcellingsImporterSettings(ImporterSettings):
    """
    """


class ParcellingsImporterFromImportSettings(ImporterFromSettingsForm):

    def __init__(self, settings_form, importer_class=ParcellingsImporter):
        """
        """
        super(ParcellingsImporterFromImportSettings, self).__init__(settings_form, importer_class)
