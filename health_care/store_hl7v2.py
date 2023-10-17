from call_the_api import project_id


def create_hl7v2_store(project_id, location, dataset_id, hl7v2_store_id):
    """Creates a new HL7v2 store within the parent dataset.
    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
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
    # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
    # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
    hl7v2_store_parent = "projects/{}/locations/{}/datasets/{}".format(
        project_id, location, dataset_id
    )

    # Use the V3 parser. Immutable after HL7v2 store creation.
    body = {"parserConfig": {"version": "V3"}}

    request = (
        client.projects()
        .locations()
        .datasets()
        .hl7V2Stores()
        .create(parent=hl7v2_store_parent, body=body, hl7V2StoreId=hl7v2_store_id)
    )

    response = request.execute()
    print(f"Created HL7v2 store: {hl7v2_store_id}")
    return response


create_hl7v2_store(
    project_id=project_id,
    location="us-central1",
    dataset_id="first_dataset",
    hl7v2_store_id="fd_hlv72id1",
)
