from googleapiclient.discovery import build

# service account
from google.oauth2 import service_account


SERVICE_ACCOUNT_FILE = 'k.json'
SCOPES = ['']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# If modifying these scopes, delete the file token.json.


# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ''

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
#Get all minus first row because its the one with the names

#Gotta update the range for the months you need to WE WILL UPDATE THIS LATER TO AVOID INSERTING IT MANUALLY
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="").execute()
values = result.get('values', [])
