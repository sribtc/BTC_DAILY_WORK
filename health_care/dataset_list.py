# Imports the Dict and List types for runtime type hints.
from typing import Dict, List
from call_the_api import project_id


def list_datasets(project_id: str, location: str) -> List[Dict[str, str]]:
    """Lists the datasets in the project.

    See
    https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
    before running the sample.
    See https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#list
    for the Python API reference.

    Args:
      project_id: The project ID or project number of the Google Cloud project you want
          to use.
      location: The name of the location where the datasets are located.

    Returns:
      A list of Dataset resources.
    """
    # Imports HttpError from the Google Python API client errors module.
    # Imports the Google API Discovery Service.
    from googleapiclient import discovery
    from googleapiclient.errors import HttpError

    api_version = "v1"
    service_name = "healthcare"
    # Returns an authorized API client by discovering the Healthcare API
    # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
    client = discovery.build(service_name, api_version)

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = 'my-project'
    # location = 'us-central1'
    dataset_parent = f"projects/{project_id}/locations/{location}"

    datasets = []
    request = client.projects().locations().datasets().list(parent=dataset_parent)
    while request is not None:
        try:
            response = request.execute()
            if response and "datasets" in response:
                datasets.extend(response["datasets"])
            # Paginate over results until the list_next() function returns None.
            request = (
                client.projects()
                .locations()
                .datasets()
                .list_next(previous_request=request, previous_response=response)
            )

            for dataset in datasets:
                print(
                    f"Dataset: {dataset.get('name')}\nTime zone: {dataset.get('timeZone')}"
                )

            return datasets

        except HttpError as err:
            raise err
