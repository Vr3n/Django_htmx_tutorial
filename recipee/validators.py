from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError

valid_unit_measurements = [
    "pounds",
    'lbs',
    'oz',
    'gram'
]

def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"{e} does not have valid measure of unit.")
    except:
        raise ValidationError(f"{value} does not have valid measure of unit.")

# aise ValidationError(f"{value} does not have valid measure of unit.\nValid units are: {', '.join(valid_unit_measurements)}")