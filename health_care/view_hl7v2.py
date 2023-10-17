from call_the_api import project_id


def get_hl7v2_message(
    project_id, location, dataset_id, hl7v2_store_id, hl7v2_message_id
):
    """Gets an HL7v2 message.

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
    # hl7v2_message_id = '2yqbdhYHlk_ucSmWkcKOVm_N0p0OpBXgIlVG18rB-cw='  # replace with the HL7v2 message ID that was returned by the server
    hl7v2_parent = f"projects/{project_id}/locations/{location}"
    hl7v2_message_name = "{}/datasets/{}/hl7V2Stores/{}/messages/{}".format(
        hl7v2_parent, dataset_id, hl7v2_store_id, hl7v2_message_id
    )

    msgs = client.projects().locations().datasets().hl7V2Stores().messages()
    message = msgs.get(name=hl7v2_message_name).execute()

    print("Name: {}".format(message.get("name")))
    print("Data: {}".format(message.get("data")))
    print("Creation time: {}".format(message.get("createTime")))
    print("Sending facility: {}".format(message.get("sendFacility")))
    print("Time sent: {}".format(message.get("sendTime")))
    print("Message type: {}".format(message.get("messageType")))
    print("Patient IDs:")
    patient_ids = message.get("patientIds")
    for patient_id in patient_ids:
        print("\tPatient value: {}".format(patient_id.get("value")))
        print("\tPatient type: {}".format(patient_id.get("type")))
    print("Labels: {}".format(message.get("labels")))

    print(message)
    return message


get_hl7v2_message(
    project_id=project_id,
    location="us-central1",
    dataset_id="first_dataset",
    hl7v2_store_id="fd_hlv72id1",
    hl7v2_message_id="TVNIfF5+XCZ8QXxTRU5EX0ZBQ0lMSVRZfEF8QXwyMDE4MDEwMTAwMDAwMHx8VFlQRV5BfDIwMTgwMTAxMDAwMDAwfFR8MC4wfHx8QUF8fDAwfEFTQ0lJDUVWTnxBMDB8MjAxODAxMDEwNDAwMDANUElEfHwxNAExMTFeXl5eTVJOfDExMTExMTExXl5eXk1STn4xMTExMTExMTExXl5eXk9SR05NQlI=",
)
