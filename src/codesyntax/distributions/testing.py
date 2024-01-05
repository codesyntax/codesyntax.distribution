# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PLONE_FIXTURE,
    PloneSandboxLayer,
)
from plone.testing import z2

import codesyntax.distributions


class CodesyntaxDistributionsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.app.dexterity

        self.loadZCML(package=plone.app.dexterity)
        import plone.restapi

        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=codesyntax.distributions)

    def setUpPloneSite(self, portal):
        applyProfile(portal, "codesyntax.distributions:default")


CODESYNTAX_DISTRIBUTIONS_FIXTURE = CodesyntaxDistributionsLayer()


CODESYNTAX_DISTRIBUTIONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(CODESYNTAX_DISTRIBUTIONS_FIXTURE,),
    name="CodesyntaxDistributionsLayer:IntegrationTesting",
)


CODESYNTAX_DISTRIBUTIONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(CODESYNTAX_DISTRIBUTIONS_FIXTURE,),
    name="CodesyntaxDistributionsLayer:FunctionalTesting",
)


CODESYNTAX_DISTRIBUTIONS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        CODESYNTAX_DISTRIBUTIONS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name="CodesyntaxDistributionsLayer:AcceptanceTesting",
)
