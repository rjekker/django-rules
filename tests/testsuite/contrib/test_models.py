from __future__ import absolute_import

import sys
import unittest

from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import get_object_or_404
from django.test import TestCase

import rules

from . import TestData

if sys.version_info.major >= 3:
    from testapp.models import Car


@unittest.skipIf(sys.version_info.major < 3, "Python 3 only")
class RulesModelTests(TestData, TestCase):
    def test_preprocess(self):
        from testapp.models import TestModel

        self.assertTrue(rules.perm_exists("testapp.add_testmodel"))
        self.assertTrue(rules.perm_exists("testapp.custom_testmodel"))

    def test_invalid_config(self):
        from rules.contrib.models import RulesModel

        with self.assertRaises(ImproperlyConfigured):

            class InvalidTestModel(RulesModel):
                class Meta:
                    app_label = "testapp"
                    rules_permissions = "invalid"

    def test_cars_owner(self):
        # adrian can *not* drive martins car
        car1 = Car.objects.get(pk=1)
        assert car1.owner.username == "adrian"
        car2 = Car.objects.get(pk=2)
        assert car2.owner.username == "martin"
        adrian = get_user_model().objects.get(pk=1)
        martin = get_user_model().objects.get(pk=2)
        assert adrian == car1.owner
        assert martin == car2.owner

        assert not adrian.has_perm(Car.get_perm("drive"), car2)
        assert not martin.has_perm(Car.get_perm("drive"), car1)
