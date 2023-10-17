from call_the_api import project_id


def ingest_hl7v2_message(
    project_id, location, dataset_id, hl7v2_store_id, hl7v2_message_file
):
    """Ingests a new HL7v2 message from the hospital and sends a notification
    to the Cloud Pub/Sub topic. Return is an HL7v2 ACK message if the message
    was successfully stored.

    See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
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
    # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
    # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
    # hl7v2_message_file = 'hl7v2-message.json'  # replace with the path to the HL7v2 file
    hl7v2_parent = f"projects/{project_id}/locations/{location}"
    hl7v2_store_name = "{}/datasets/{}/hl7V2Stores/{}".format(
        hl7v2_parent, dataset_id, hl7v2_store_id
    )

    with open(hl7v2_message_file) as hl7v2_message:
        hl7v2_message_content = json.load(hl7v2_message)

    request = (
        client.projects()
        .locations()
        .datasets()
        .hl7V2Stores()
        .messages()
        .ingest(parent=hl7v2_store_name, body=hl7v2_message_content)
    )

    response = request.execute()
    print(f"Ingested HL7v2 message from file: {hl7v2_message_file}")
    return response


ingest_hl7v2_message(
    project_id=project_id,
    location="us-central1",
    dataset_id="first_dataset",
    hl7v2_store_id="fd_hlv72id1",
    hl7v2_message_file=r"C:\Users\Sriharsha\Documents\healthcare_api\hl7v2-sample.json".replace(
        "\\", "/"
    ),
)
