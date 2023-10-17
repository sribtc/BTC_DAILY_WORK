from requests import HTTPError
from call_the_api import *
import time

# Imports the Dict type for runtime type hints.
from typing import Dict

client = service


def create_dataset(project_id: str, location: str, dataset_id: str) -> Dict[str, str]:
    """Creates a Cloud Healthcare API dataset.

    See
    https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
    before running the sample.
    See
    https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#create
    for the Python API reference.

    Args:
      project_id: The project ID or project number of the Google Cloud project you want
          to use.
      location: The name of the dataset's location.
      dataset_id: The ID of the dataset to create.

    Returns:
      A dictionary representing a long-running operation that results from
      calling the 'CreateDataset' method. Dataset creation is typically fast.
    """

    # TODO(developer): Uncomment these lines and replace with your values.
    # project_id = project_id
    # location = 'us-central1'
    # dataset_id = 'my-dataset'
    dataset_parent = f"projects/{project_id}/locations/{location}"

    request = (
        client.projects()
        .locations()
        .datasets()
        .create(parent=dataset_parent, body={}, datasetId=dataset_id)
    )

    # Wait for operation to complete.
    start_time = time.time()
    max_time = 600  # 10 minutes, but dataset creation is typically only a few seconds.

    try:
        operation = request.execute()
        while not operation.get("done", False):
            # Poll until the operation finishes.
            print("Waiting for operation to finish...")
            if time.time() - start_time > max_time:
                raise TimeoutError("Timed out waiting for operation to finish.")
            operation = (
                client.projects()
                .locations()
                .datasets()
                .operations()
                .get(name=operation["name"])
                .execute()
            )
            # Wait 5 seconds between each poll to the operation.
            time.sleep(5)

        if "error" in operation:
            raise RuntimeError(f"Create dataset operation failed: {operation['error']}")
        else:
            dataset_name = operation["response"]["name"]
            print(f"Created dataset: {dataset_name}")
            return operation

    except HTTPError as err:
        # A common error is when the dataset already exists.
        if err.resp.status == 409:
            print(f"Dataset with ID {dataset_id} already exists.")
            return
        else:
            raise err


create_dataset(
    project_id=project_id, location="us-central1", dataset_id="instanced_example"
)
