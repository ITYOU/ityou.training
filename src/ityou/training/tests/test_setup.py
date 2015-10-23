# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from ityou.training.testing import ITYOU_TRAINING_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that ityou.training is properly installed."""

    layer = ITYOU_TRAINING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if ityou.training is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('ityou.training'))

    def test_browserlayer(self):
        """Test that IItyouTrainingLayer is registered."""
        from ityou.training.interfaces import IItyouTrainingLayer
        from plone.browserlayer import utils
        self.assertIn(IItyouTrainingLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ITYOU_TRAINING_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['ityou.training'])

    def test_product_uninstalled(self):
        """Test if ityou.training is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('ityou.training'))

    def test_browserlayer_removed(self):
        """Test that IItyouTrainingLayer is removed."""
        from ityou.training.interfaces import IItyouTrainingLayer
        from plone.browserlayer import utils
        self.assertNotIn(IItyouTrainingLayer, utils.registered_layers())
