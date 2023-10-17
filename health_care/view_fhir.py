from call_the_api import project_id
import json


def search_resources_get(
    project_id,
    location,
    dataset_id,
    fhir_store_id,
    resource_type,
):
    """
    Uses the searchResources GET method to search for resources in the given FHIR store.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
    before running the sample."""
    # Imports Python's built-in "os" module
    import os

    # Imports the google.auth.transport.requests transport
    from google.auth.transport import requests

    # Imports a module to allow authentication using a service account
    from google.oauth2 import service_account

    # Gets credentials from the environment.
    credentials = service_account.Credentials.from_service_account_file(
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
    )
    scoped_credentials = credentials.with_scopes(
        ["https://www.googleapis.com/auth/cloud-platform"]
    )
    # Creates a requests Session object with the credentials.
    session = requests.AuthorizedSession(scoped_credentials)

    # URL to the Cloud Healthcare API endpoint and version
    base_url = "https://healthcare.googleapis.com/v1"

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the parent dataset's location
    # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
    # fhir_store_id = 'my-fhir-store' # replace with the FHIR store ID
    # resource_type = 'Patient'  # replace with the FHIR resource type
    url = f"{base_url}/projects/{project_id}/locations/{location}"

    resource_path = "{}/datasets/{}/fhirStores/{}/fhir/{}".format(
        url, dataset_id, fhir_store_id, resource_type
    )

    response = session.get(resource_path)
    response.raise_for_status()

    resources = response.json()

    print(
        "Using GET request, found a total of {} {} resources:".format(
            resources["total"], resource_type
        )
    )
    print(json.dumps(resources, indent=2))

    return resources


search_resources_get(
    project_id=project_id,
    location="us-central1",
    dataset_id="first_dataset",
    fhir_store_id="fd_fhirid1",
    resource_type="Patient",
)
