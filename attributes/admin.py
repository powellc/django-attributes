from django.contrib import admin
from attributes.models import AttributeOption
from attributes.utils import validate_attribute_value

def clean_attribute_value(cleaned_data, obj):
    value = cleaned_data['value']
    attribute = cleaned_data['option']
    success, valid_value = validate_attribute_value(attribute, value, obj)
    if not success:
        raise ValidationError(attribute.error_message)
    
    return valid_value

admin.site.register(AttributeOption)
