# Imports the Dict type for runtime type hints.
from call_the_api import project_id
from typing import Dict


def patch_dataset(
    project_id: str, location: str, dataset_id: str, time_zone: str
) -> Dict[str, str]:
    """Updates dataset metadata.

    See
    https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
    before running the sample.
    See https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#patch
    for the Python API reference.

    Args:
      project_id: The project ID or project number of the Google Cloud project you want
          to use.
      location: The name of the dataset's location.
      dataset_id: The ID of the dataset to patch.
      time_zone: The default timezone used by the dataset.

    Returns:
      A dictionary representing the patched Dataset resource.
    """
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery

    # Imports HttpError from the Google Python API client errors module.
    from googleapiclient.errors import HttpError

    api_version = "v1"
    service_name = "healthcare"
    # Returns an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'
    # location = 'us-central1'
    # dataset_id = 'my-dataset'
    # time_zone = 'GMT'
    dataset_parent = f"projects/{project_id}/locations/{location}"
    dataset_name = f"{dataset_parent}/datasets/{dataset_id}"

    # Sets the time zone
    patch = {"timeZone": time_zone}

    request = (
        client.projects()
        .locations()
        .datasets()
        .patch(name=dataset_name, updateMask="timeZone", body=patch)
    )

    try:
        response = request.execute()
        print(f"Patched dataset {dataset_id} with time zone: {time_zone}")
        return response
    except HttpError as err:
        raise err
