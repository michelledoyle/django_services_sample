from django.shortcuts import render
from django.utils.timezone import now

from services.models.models import Encounters, Patient


def encounter(request):
    encounter_model = Encounters(
        encounter_id=13334440,
        person_id=166778933,
        first_name="Fushun",
        last_name="Django in CloudRun",
        zip_code="300013",
        sp_load_time_stamp=now()
    )
    encounter_model.save()
    return render(request, 'success.html')  # Create a success template

#
# def patient(request):
#     patient_model = Patient(
#         resource_type="patient",
#         patient_id="100001",
#         name="patient Jane",
#         gender="F",
#         street="101 Main St",
#         city="Atlanta",
#         zip_code="239904",
#     )
#     patient_model.save()
#     return render(request, 'success.html')  # Create a success template
