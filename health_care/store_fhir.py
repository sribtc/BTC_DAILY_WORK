from call_the_api import project_id


def create_fhir_store(project_id, location, dataset_id, fhir_store_id, version):
    """Creates a new FHIR store within the parent dataset.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
    before running the sample."""
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    api_version = "v1"
    service_name = "healthcare"
    # Returns an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the parent dataset's location
    # dataset_id = 'my-dataset'  # replace with the FHIR store's parent dataset ID
    # fhir_store_id = 'my-fhir-store'  # replace with the FHIR store's ID
    # version = 'R4'  # replace with the FHIR store version
    fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )

    body = {"version": version}

    request = (
        client.projects()
        .locations()
        .datasets()
        .fhirStores()
        .create(parent=fhir_store_parent, body=body, fhirStoreId=fhir_store_id)
    )

    response = request.execute()
    print(f"Created FHIR store: {fhir_store_id}")

    return response


create_fhir_store(
    project_id=project_id,
    location="us-central1",
    dataset_id="first_dataset",
    fhir_store_id="fd_fhirid1",
    version="R4",
)
