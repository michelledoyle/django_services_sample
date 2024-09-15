#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from services.spanner_to_pubsub import SpannerToPubSubPublisherService
from services.pubsub_to_spanner import PubSubToSpannerListenerService


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'services_project.settings')
    os.environ.setdefault('GOOGLE_CLOUD_PROJECT', 'asc-ahnat-rthe-sandbox-poc')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Publisher Service for Cloud Spanner
    PROJECT_ID = "asc-ahnat-rthe-sandbox-poc"
    INSTANCE_ID = "the-poc1"
    DATABASE_ID = "rthe-poc1"
    PUBSUB_TOPIC_ID = "poc-topic-outbound"
    TABLE_NAME = "Encounters"

    # # Listener Service for Cloud Spanner
    # listener = PubSubToSpannerListenerService(
    #     project_id=PROJECT_ID,
    #     subscription_id="poc-topic-inbound-sub",
    #     instance_id=INSTANCE_ID,
    #     database_id=DATABASE_ID,
    #     table_name=TABLE_NAME,
    #     timeout=3600.0
    # )
    #
    # # Start listening for messages
    # listener.listen_for_messages()

    # Create an instance of the SpannerPubSubService
    publish_service = SpannerToPubSubPublisherService(PROJECT_ID, INSTANCE_ID, DATABASE_ID, PUBSUB_TOPIC_ID, TABLE_NAME)
    print(f"``````topic is this````````` {PUBSUB_TOPIC_ID}")
    # Execute the service
    publish_service.execute()

    main()
