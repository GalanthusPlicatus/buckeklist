from __future__ import unicode_literals

from flufl.enum import IntEnum
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StatusEnum(IntEnum):
    unknown = 0
    created = 1
    planned = 2
    prosessing = 3
    postponed = 4
    achieved = 5
    dropped = 6


class VisibilityEnum(IntEnum):
    unknown = 0
    public = 1
    private = 2
    shared = 3


class Dream(models.Model):
    STATUS_CHOICES = [(int(enum_choice), enum_choice.name) for enum_choice in StatusEnum]
    VISIBILITY_CHOICES = [(int(enum_choice), enum_choice.name) for enum_choice in VisibilityEnum]

    name = models.CharField(max_length=200)
    description = models.CharField(null=True, blank=True, max_length=255)
    visiblity = models.PositiveSmallIntegerField(
        choices=VISIBILITY_CHOICES,
        default=int(VisibilityEnum.unknown)
    )
    status = models.PositiveSmallIntegerField(
        choices=STATUS_CHOICES,
        default=int(StatusEnum.created)
    )
    created_by = models.ForeignKey(User, blank=True, null=True, related_name="dreamer", on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    updated_at = models.DateTimeField(auto_now=True, null=True)


