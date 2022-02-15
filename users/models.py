from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # WARNING!
    """
    Some officially supported features of Crowdbotics Dashboard depend on the initial
    state of this User model (Such as the creation of superusers using the CLI
    or password reset in the dashboard). Changing, extending, or modifying this model
    may lead to unexpected bugs and or behaviors in the automated flows provided
    by Crowdbotics. Change it at your own risk.


    This model represents the User instance of the system, login system and
    everything that relates with an `User` is represented by this model.
    """
    name = models.CharField(
        null=True,
        blank=True,
        max_length=255,
    )
    mrn = models.TextField(
        null=True,
        blank=True,
    )
    twi_partnumber = models.TextField(
        null=True,
        blank=True,
    )
    lgth = models.IntegerField(
        null=True,
        blank=True,
    )
    units = models.TextField(
        null=True,
        blank=True,
    )
    org_lgth = models.TextField(
        null=True,
        blank=True,
    )
    workOrder = models.IntegerField(
        null=True,
        blank=True,
    )
    vender = models.TextField(
        null=True,
        blank=True,
    )
    lotNumber = models.BigIntegerField(
        null=True,
        blank=True,
    )
    rollNumber = models.BigIntegerField(
        null=True,
        blank=True,
    )
    useByDate = models.DateField(
        null=True,
        blank=True,
    )
    supMfgDate = models.DateField(
        null=True,
        blank=True,
    )
    recievedDate = models.DateField(
        null=True,
        blank=True,
    )
    size = models.TextField(
        null=True,
        blank=True,
    )
    shelfLife = models.IntegerField(
        null=True,
        blank=True,
    )
    mpn = models.TextField(
        null=True,
        blank=True,
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
