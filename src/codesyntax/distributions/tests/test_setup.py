# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from codesyntax.distributions.testing import (
    CODESYNTAX_DISTRIBUTIONS_INTEGRATION_TESTING,
)  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that codesyntax.distributions is properly installed."""

    layer = CODESYNTAX_DISTRIBUTIONS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if codesyntax.distributions is installed."""
        self.assertTrue(self.installer.is_product_installed("codesyntax.distributions"))

    def test_browserlayer(self):
        """Test that ICodesyntaxDistributionsLayer is registered."""
        from codesyntax.distributions.interfaces import ICodesyntaxDistributionsLayer
        from plone.browserlayer import utils

        self.assertIn(ICodesyntaxDistributionsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = CODESYNTAX_DISTRIBUTIONS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("codesyntax.distributions")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if codesyntax.distributions is cleanly uninstalled."""
        self.assertFalse(
            self.installer.is_product_installed("codesyntax.distributions")
        )

    def test_browserlayer_removed(self):
        """Test that ICodesyntaxDistributionsLayer is removed."""
        from codesyntax.distributions.interfaces import ICodesyntaxDistributionsLayer
        from plone.browserlayer import utils

        self.assertNotIn(ICodesyntaxDistributionsLayer, utils.registered_layers())
