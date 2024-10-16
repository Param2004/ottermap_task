from django.db import models
from django.core.exceptions import ValidationError

def validate_latitude(value):
    """Ensure latitude is between -90 and 90 degrees."""
    if value < -90 or value > 90:
        raise ValidationError('Latitude must be between -90 and 90.')

def validate_longitude(value):
    """Ensure longitude is between -180 and 180 degrees."""
    if value < -180 or value > 180:
        raise ValidationError('Longitude must be between -180 and 180.')

class Shop(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField(validators=[validate_latitude])
    longitude = models.FloatField(validators=[validate_longitude])

    def __str__(self):
        return self.name
