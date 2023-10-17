from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
SERVICE_ACCOUNT_FILE = r"C:\Users\Sriharsha\Downloads\healthcare-exp-174ecacaa6dc.json".replace('\\','/')


credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)
service = build('healthcare','v1',credentials=credentials)


project_id = credentials.project_id
service_account_email = credentials.service_account_email

