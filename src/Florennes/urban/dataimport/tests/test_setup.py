# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from Florennes.urban.dataimport.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of Florennes.urban.dataimport into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if Florennes.urban.dataimport is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('Florennes.urban.dataimport'))

    def test_uninstall(self):
        """Test if Florennes.urban.dataimport is cleanly uninstalled."""
        self.installer.uninstallProducts(['Florennes.urban.dataimport'])
        self.assertFalse(self.installer.isProductInstalled('Florennes.urban.dataimport'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IFlorennesUrbanDataimportLayer is registered."""
        from Florennes.urban.dataimport.interfaces import IFlorennesUrbanDataimportLayer
        from plone.browserlayer import utils
        self.failUnless(IFlorennesUrbanDataimportLayer in utils.registered_layers())
