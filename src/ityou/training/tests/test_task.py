# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from ityou.training.testing import ITYOU_TRAINING_INTEGRATION_TESTING  # noqa
from ityou.training.interfaces import ITask

import unittest2 as unittest


class TaskIntegrationTest(unittest.TestCase):

    layer = ITYOU_TRAINING_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Task')
        schema = fti.lookupSchema()
        self.assertEqual(ITask, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Task')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Task')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ITask.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Task', 'Task')
        self.assertTrue(
            ITask.providedBy(self.portal['Task'])
        )
