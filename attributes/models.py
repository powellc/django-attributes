import logging
import datetime
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db import models
# Support the user's setting of custom expressions in the settings.py file
try:
        user_validations = settings.get('ATTRIBUTE_VALIDATIONS')
except:
        user_validations = None

VALIDATIONS = [
       ('attributes.utils.validation_simple', _('One or more characters')),
       ('attributes.utils.validation_integer', _('Integer number')),
       ('attributes.utils.validation_yesno', _('Yes or No')),
       ('attributes.utils.validation_decimal', _('Decimal number')),
]

if user_validations:
    VALIDATIONS.extend(user_validations)

class AttributeOption(models.Model):
    """
    Allows arbitrary name/value pairs to be attached to a model.
    By defining the list, the user will be presented with a predefined
    list of attributes instead of a free form field.
    The validation field should contain a regular expression that can be
    used to validate the structure of the input.
    """
    description = models.CharField(_("Description"), max_length=100)
    name = models.SlugField(_("Attribute name"), max_length=100)
    validation = models.CharField(_("Field Validations"), choices=VALIDATIONS, max_length=100)
    sort_order = models.IntegerField(_("Sort Order"), default=1)
    error_message = models.CharField(_("Error Message"), default=_("Invalid Entry"), max_length=100)
                                                                        
    class Meta:
        pass

    def __unicode__(self):
        return self.description

class BaseAttribute(models.Model):
    """
    Allows arbitrary name/value pairs (as strings) to be attached to a product.
    """
    option = models.ForeignKey(AttributeOption)
    value = models.CharField(_('Value'), max_length=255)

    def _name(self):
        return self.option.name
    name = property(_name)

    def _description(self):
        return self.option.description
    description = property(_description)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.option.name


