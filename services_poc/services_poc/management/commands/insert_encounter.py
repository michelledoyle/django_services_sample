from django.core.management.base import BaseCommand
from services_poc.services_poc.models.encounters import encounters  # Replace 'myapp' with your app name
from services_poc.services_poc.models.encounters.encounters import Encounter


class Command(BaseCommand):
    help = 'Insert an encounter record into the Encounter table'

    def handle(self, *args, **kwargs):
        Encounter.objects.create(
            encounter_id=44555,
            person_id=312300,
            first_name="Ramen",
            last_name="Django"
        )
        self.stdout.write(self.style.SUCCESS('Encounter inserted successfully!'))
