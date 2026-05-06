from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


# Custom Validators

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(f'Число {value} нечетное', code='odd', params={'value': value})

class MinMaxValueValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or value > self.max_value:
            raise ValidationError('Введенное вами число находится в диапозоне от %(min)s до %(max)s',
                                  code='out_of_range',
                                  params={'min': self.min_value, 'max': self.max_value})

def get_min_length(value):
    return value