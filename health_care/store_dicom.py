from call_the_api import *


def create_dicom_store(project_id, location, dataset_id, dicom_store_id):
    client = service
    """Creates a new DICOM store within the parent dataset.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
    before running the sample."""

    # project_id = 'my-project'  # replace with your GCP project ID
    # location = 'us-central1'  # replace with the parent dataset's location
    # dataset_id = 'my-dataset'  # replace with the DICOM store's parent dataset ID
    # dicom_store_id = 'my-dicom-store'  # replace with the DICOM store's ID
    dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )

    request = (
        client.projects()
        .locations()
        .datasets()
        .dicomStores()
        .create(parent=dicom_store_parent, body={}, dicomStoreId=dicom_store_id)
    )

    response = request.execute()
    print(f"Created DICOM store: {dicom_store_id}")
    return response


create_dicom_store(
    project_id=project_id,
    location="us-central1",
    dataset_id="instanced_example",
    dicom_store_id="first_instance",
)
