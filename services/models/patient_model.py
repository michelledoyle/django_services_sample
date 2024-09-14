from django.db import models


class Patient(models.Model):
    resource_type = models.CharField(max_length=50)
    patient_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'Patient'

    def __str__(self):
        return f"{self.name} {self.gender}"
