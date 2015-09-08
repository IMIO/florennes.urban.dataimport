# -*- coding: utf-8 -*-

from imio.urban.dataimport.browser.controlpanel import ImporterControlPanel
from imio.urban.dataimport.browser.import_panel import ImporterSettings
from imio.urban.dataimport.browser.import_panel import ImporterSettingsForm
from imio.urban.dataimport.acropole.settings import AcropoleImporterFromImportSettings


class FlorennesImporterSettingsForm(ImporterSettingsForm):
    """ """

class FlorennesImporterSettings(ImporterSettings):
    """ """
    form = FlorennesImporterSettingsForm


class FlorennesImporterControlPanel(ImporterControlPanel):
    """ """
    import_form = FlorennesImporterSettings


class FlorennesImporterFromImportSettings(AcropoleImporterFromImportSettings):
    """ """

    def get_importer_settings(self):
        """
        Return the db name to read.
        """
        settings = super(FlorennesImporterFromImportSettings, self).get_importer_settings()

        db_settings = {
            'db_name': '',
        }

        settings.update(db_settings)

        return settings
