from call_the_api import project_id


def get_dicom_store(project_id, location, dataset_id, dicom_store_id):
    """Gets the specified DICOM store.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
    before running the sample."""
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    # Imports Python's built-in "json" module
    import json

    api_version = "v1"
    service_name = "healthcare"
    # Returns an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the parent dataset's location
    # dataset_id = 'my-dataset'  # replace with the DICOM store's parent dataset ID
    # dicom_store_id = 'my-dicom-store'  # replace with the DICOM store's ID
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )
    dicom_store_name = f"{dicom_store_parent}/dicomStores/{dicom_store_id}"

    dicom_stores = client.projects().locations().datasets().dicomStores()
    dicom_store = dicom_stores.get(name=dicom_store_name).execute()

    print(json.dumps(dicom_store, indent=2))
    return dicom_store


store = get_dicom_store(
    project_id=project_id,
    location="us-central1",
    dataset_id="NIHR",
    dicom_store_id="first",
)

print(store)
print(type(store))
