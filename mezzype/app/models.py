# python import
import datetime

# django import
from django.db import models
from django.utils.translation import ugettext_lazy as _

# edc import
from emencia.django.countries.models import Country

# userena import
from userena.models import UserenaLanguageBaseProfile


class Profile(UserenaLanguageBaseProfile):
    GENDER_CHOICES = (
        (1, _('Male')),
        (2, _('Female')),
    )
    gender = models.PositiveSmallIntegerField(
            _('gender'), choices=GENDER_CHOICES, blank=True, null=True)

    # Contact
    phone = models.CharField(_('phone'), max_length=40, blank=True, null=True)

    # Address
    address_1 = models.TextField(_('address 1'), blank=True)
    address_2 = models.TextField(_('address 2'), blank=True, null=True)
    address_comments = models.TextField(_('address comments'), blank=True,
            null=True)
    postal_code = models.CharField(_('postal code'), max_length=20, blank=True)
    city = models.CharField(_('city'), max_length=255, blank=True)
    country = models.ForeignKey(Country, verbose_name=_('country'), null=True)

    # additional info
    birthdate = models.DateField(_('birthdate'),
            help_text=_('yyyy-mm-dd format'), blank=True, null=True)
    website = models.URLField(_('website'), blank=True, verify_exists=True,
            null=True)
    about_me = models.TextField(_('about me'), blank=True, null=True)

    @property
    def age(self):
        if not self.birth_date: return False
        else:
            today = datetime.date.today()
            # Raised when birth date is February 29 and the current year is not a
            # leap year.
            try:
                birthday = self.birth_date.replace(year=today.year)
            except ValueError:
                day = today.day - 1 if today.day != 1 else today.day + 2
                birthday = self.birth_date.replace(year=today.year, day=day)
            if birthday > today: return today.year - self.birth_date.year - 1
            else: return today.year - self.birth_date.year
