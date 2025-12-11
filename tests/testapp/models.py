from __future__ import absolute_import

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

import rules
from rules.contrib.models import RulesModel


class Book(models.Model):
    isbn = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TestModel(RulesModel):
    class Meta:
        rules_permissions = {"add": rules.always_true, "view": rules.always_true}

    @classmethod
    def preprocess_rules_permissions(cls, perms):
        perms["custom"] = rules.always_true


@rules.predicate
def is_car_owner(user, car):
    return car.owner == user


class Car(RulesModel):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        rules_permissions = {
            "wash": rules.always_allow,
            "drive": is_car_owner,
            "crash": rules.always_deny,
        }
