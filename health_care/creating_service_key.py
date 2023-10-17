import os

from google.oauth2 import service_account
import googleapiclient.discovery


def create_key(service_account_email:str)-> None:


    credentials = service_account.Credentials.from_service_account_file(filename=os.environ["GOOGLE_APPLICATION_CREDENTIALS"],scopes=["https://www.googleapis.com/auth/cloud-platform"])

    service = googleapiclient.discovery.build("iam", "v1", credentials=credentials)

    key = (
        service.projects()
        .serviceAccounts()
        .keys()
        .create(name="projects/-/serviceAccounts/" + service_account_email, body={})
        .execute()
    )

    # print(key)
    print(type(key))
    print(key.keys())
    
    # if not key["disabled"]:
    #     print("Created json key")

create_key("exp-healthare2@healthcare-exp.iam.gserviceaccount.com")