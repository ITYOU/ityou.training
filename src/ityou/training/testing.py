# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ityou.training


class ItyouTrainingLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=ityou.training)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ityou.training:default')


ITYOU_TRAINING_FIXTURE = ItyouTrainingLayer()


ITYOU_TRAINING_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ITYOU_TRAINING_FIXTURE,),
    name='ItyouTrainingLayer:IntegrationTesting'
)


ITYOU_TRAINING_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ITYOU_TRAINING_FIXTURE,),
    name='ItyouTrainingLayer:FunctionalTesting'
)


ITYOU_TRAINING_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ITYOU_TRAINING_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ItyouTrainingLayer:AcceptanceTesting'
)
