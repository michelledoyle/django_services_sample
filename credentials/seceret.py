from google.cloud import secretmanager

def create_secret(project_id, secret_id, secret_value):
    """
    Create a new secret in Google Cloud Secret Manager and add a version with the given secret value.
    """
    client = secretmanager.SecretManagerServiceClient()

    # Define the secret's resource name
    parent = f"projects/{project_id}"

    # Create the secret
    secret = client.create_secret(
        parent=parent,
        secret_id=secret_id,
        secret={
            "replication": {"automatic": {}}
        }
    )

    # Add a secret version
    payload = secret_value.encode("UTF-8")
    client.add_secret_version(
        parent=secret.name,
        payload={"data": payload}
    )

    return secret.name

# Example usage
project_id = "your-gcp-project-id"
secret_id = "Michelle-rth-secret"
secret_value = "your-secret-value"
secret_name = create_secret(project_id, secret_id, secret_value)

print(f"Created secret: {secret_name}")
