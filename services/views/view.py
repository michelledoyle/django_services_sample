from django.shortcuts import render
from django.utils.timezone import now
from services.models.encounter_model import Encounters

# def encounter(request):
# encounter_model = Encounters(
#     encounter_id=1290,
#     person_id=17783,
#     first_name="Fushun",
#     last_name="Django in CloudRun from view",
#     zip_code="300013",
#     sp_load_time_stamp=now()
# )
# encounter_model.save()
# return render(request, 'success.html')  # Create a success template

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
import json
from django.http import JsonResponse
from django.utils.timezone import now


def encounter(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)

            # Create an Encounters instance with the data from the request
            encounter_model = Encounters(
                encounter_id=data.get('encounter_id', None),
                person_id=data.get('person_id', None),
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                zip_code=data.get('zip_code', ''),
                sp_load_time_stamp=now()
            )

            # Save the instance to the database
            encounter_model.save()

            return JsonResponse({"message": "Encounter saved successfully!"}, status=201)

        except (KeyError, ValueError, json.JSONDecodeError) as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=405)
