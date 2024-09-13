from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Assuming User model is used for users


class Encounter(models.Model):
    # Encounter-specific fields
    encounter_id = models.IntegerField(primary_key=True)  # Assuming this is the unique identifier for each encounter
    person_id = models.IntegerField()  # ID of the person involved in the encounter

    # Person-related fields
    first_name = models.CharField(max_length=100)  # Person's first name
    last_name = models.CharField(max_length=100)  # Person's last name

    # Metadata fields
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set the time when the record is created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-set the time when the record is updated

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Encounter ID: {self.encounter_id}"

    class Meta:
        ordering = ['-encounter_id']  # Ordering encounters by their ID in descending order
