from decimal import Decimal
import logging

# Custom validations can be added to the list via the setting ATTRIBUTE_VALIDATION
# See models.py for an example, attrs should be in a tuple with the path to the validation and a name

def validation_simple(value, obj=None):
    """
    Validates that at least one character has been entered.
    Not change is made to the value.
    """
    if len(value) >= 1:
        return True, value
    else:
        return False, value

def validation_integer(value, obj=None):
    """
   Validates that value is an integer number.
   No change is made to the value
    """
    try:
        check = int(value)
        return True, value
    except:
        return False, value

def validation_yesno(value, obj=None):
    """
    Validates that yes or no is entered.
    Converts the yes or no to capitalized version
    """
    if string.upper(value) in ["YES","NO"]:
        return True, string.capitalize(value)
    else:
        return False, value

def validation_decimal(value, obj=None):
    """
    Validates that the number can be converted to a decimal
    """
    try:
        check = Decimal(value)
        return True, value
    except:
        return False, value

def import_validator(validator):
    try:
        import_name, function_name = validator.rsplit('.', 1)
    except ValueError:
        # no dot; treat it as a global
        func = globals().get(validator, None)
        if not func:
            # we use ImportError to keep error handling for callers simple
            raise ImportError
        return validator
    else:
        # The below __import__() call is from python docs, and is equivalent to:
        #
        #   from import_name import function_name
        #
        import_module = __import__(import_name, globals(), locals(), [function_name])

        return getattr(import_module, function_name)

def validate_attribute_value(attribute, value, obj):
    """
    Helper function for forms that wish to validation a value for an
    AttributeOption.
    """
    return import_validator(attribute.validation)(value, obj)