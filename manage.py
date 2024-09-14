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
    # Listener Service for Cloud Spanner
    listener = PubSubToSpannerListenerService(
        project_id="asc-ahnat-rthe-sandbox-poc",
        subscription_id="poc-topic-inbound-sub",
        instance_id="the-poc1",
        database_id="rthe-poc1",
        table_name="Encounter",
        timeout=3600.0
    )

    # Start listening for messages
    listener.listen_for_messages()

    # Publisher Service for Cloud Spanner
    PROJECT_ID = "asc-ahnat-rthe-sandbox-poc"
    INSTANCE_ID = "the-poc1"
    DATABASE_ID = "rthe-poc1"
    PUBSUB_TOPIC_ID = "poc-topic-outbound"
    TABLE_NAME = "Encounter"

    # Create an instance of the SpannerPubSubService
    publish_service = SpannerToPubSubPublisherService(PROJECT_ID, INSTANCE_ID, DATABASE_ID, PUBSUB_TOPIC_ID, TABLE_NAME)

    # Execute the service
    publish_service.execute()

    main()
