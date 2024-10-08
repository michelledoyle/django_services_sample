import os

from google.cloud import spanner
from google.cloud import pubsub_v1
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'services_project.settings')
# Initialize Django
django.setup()


class SpannerToPubSubPublisherService:
    def __init__(self, project_id, instance_id, database_id, pubsub_topic_id, table_name):
        # Initialize Cloud Spanner client
        self.spanner_client = spanner.Client(project=project_id)
        self.instance = self.spanner_client.instance(instance_id)
        self.database = self.instance.database(database_id)

        # Initialize Pub/Sub publisher client
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(project_id, pubsub_topic_id)

        self.table_name = table_name

    def read_encounter_data_from_spanner(self):
        """Read encounter data from Cloud Spanner"""
        with self.database.snapshot() as snapshot:
            query = f"SELECT encounter_id, person_id, first_name, last_name, zip_code FROM {self.table_name} LIMIT 1;"
            results = snapshot.execute_sql(query)

            encounter_list = []
            for row in results:
                encounter_data = {
                    "encounter_id": row[0],
                    "person_id": row[1],
                    "first_name": row[2],
                    "last_name": row[3],
                    "zip_code": row[4]
                }
                encounter_list.append(encounter_data)

            print(f"``````encounter_data is this````````` {encounter_data}")

            return encounter_list

    def publish_to_pubsub(self, encounters):
        """Publish encounter data to a Pub/Sub topic"""
        for encounter in encounters:
            message_json = json.dumps(encounter).encode("utf-8")
            future = self.publisher.publish(self.topic_path, message_json)
            print(f"Published message ID: {future.result()}")

    def execute(self):
        # Step 1: Read data from Cloud Spanner
        encounters = self.read_encounter_data_from_spanner()
        print(f"Retrieved {len(encounters)} records from Cloud Spanner.")

        # Step 2: Publish the data to a Pub/Sub topic
        self.publish_to_pubsub(encounters)
        print(f"Published {len(encounters)} messages to Pub/Sub.")

# # If this file is run as the main program
# if __name__ == "__main__":
#     # Configuration values
#     PROJECT_ID = "asc-ahnat-rthe-sandbox-poc"
#     INSTANCE_ID = "the-poc1"
#     DATABASE_ID = "rthe-poc1"
#     PUBSUB_TOPIC_ID = "poc-topic-outbound"
#     TABLE_NAME = "Encounter"
#
#     # Create an instance of the SpannerPubSubService
#     service = SpannerToPubSubPublisherService(PROJECT_ID, INSTANCE_ID, DATABASE_ID, PUBSUB_TOPIC_ID, TABLE_NAME)
#
#     # Execute the service
#     service.execute()
