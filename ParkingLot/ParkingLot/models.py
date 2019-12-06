from django.db import models
from .constants import ParkingConst


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
        ordering = ['-id']
        default_permissions = ('add', 'change', 'delete', 'view')


class ParkingLotSlots(BaseModel):
    id = models.AutoField(primary_key=True)
    status = models.CharField(default=ParkingConst.FREE.value, max_length=10)


class ParkingDetails(BaseModel):
    slot_no = models.ForeignKey('ParkingLotSlots', on_delete=models.CASCADE)
    car_registration_number = models.CharField(max_length=40, blank=True, null=True, unique=True)
    car_color = models.CharField(max_length=20, blank=True, null=True)
