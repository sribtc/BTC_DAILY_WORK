import json
from call_the_api import project_id


def dicomweb_search_instance(project_id, location, dataset_id, dicom_store_id):
    """Handles the GET requests specified in DICOMweb standard.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
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
    # dicom_store_id = 'my-dicom-store' # replace with the DICOM store ID
    url = f"{base_url}/projects/{project_id}/locations/{location}"

    dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/instances".format(
        url, dataset_id, dicom_store_id
    )

    # Sets required application/dicom+json; charset=utf-8 header on the request
    headers = {"Content-Type": "application/dicom+json; charset=utf-8"}

    response = session.get(dicomweb_path, headers=headers)
    response.raise_for_status()

    instances = response.json()

    print("Instances:")
    print(json.dumps(instances, indent=2))

    return instances


dicomweb_search_instance(
    project_id=project_id,
    location="us-central1",
    dataset_id="first_dataset",
    dicom_store_id="fd_dicomid1",
)
