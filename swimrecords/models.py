from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

def relay_check(stroke):
    list = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in list:
        raise ValidationError(f"{stroke} is not a valid stroke")
    
def distance_check(distance):
    limit = 50
    if distance <= limit:
        raise ValidationError(f"Ensure this value is greater than or equal to {limit}.")
    
def record_date_check(record_date):
    now = timezone.now()
    if record_date > now:
        raise ValidationError("Can't set record in the future.")
    
def record_broken_check(record_broken_date):
    if record_broken_date < timezone.now():
        raise ValidationError("Can't break record before record was set.")
    
class SwimRecord(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    relay = models.BooleanField(default=False)
    stroke = models.CharField(max_length=255, validators=[relay_check])
    distance = models.IntegerField(validators=[distance_check])
    record_date = models.DateTimeField(validators=[record_date_check])
    record_broken_date = models.DateTimeField(validators=[record_broken_check])
