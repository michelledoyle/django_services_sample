from google.cloud import spanner_admin_database_v1

def list_databases():
    client = spanner_admin_database_v1.DatabaseAdminClient()
    instance_name = f"projects/asc-ahnat-rthe-sandbox-poc/instances/the-poc1"

    # List databases in the specified instance
    databases = client.list_databases(parent=instance_name)

    for db in databases:
        print(db.name)

if __name__ == "__main__":
    list_databases()
