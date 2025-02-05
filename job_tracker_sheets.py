import datetime
import os

from googleapiclient.discovery import build
from google.oauth2 import service_account

# The ID and range of the spreadsheet.
SHEET_ID = "sheet-id"  # Replace with your sheet ID
SHEET_NAME = "Sheet1"  # Replace with your sheet name
RANGE = f"{SHEET_NAME}!A:E"

# Path to your service account JSON key file.  Keep this file secure!
SERVICE_ACCOUNT_FILE = os.path.join(os.path.dirname(__file__), 'file.json')  # Replace with your path

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)

def get_application_details():
    today = datetime.date.today()  # Get today's date
    formatted_date = today.strftime("%d/%m/%Y")  # Format it

    while True:
        company = input("Enter company name: ").strip()
        if company:
            break
        else:
            print("Company name cannot be empty. Please try again.")

    while True:
        position = input("Enter position title: ").strip()
        if position:
            break
        else:
            print("Position title cannot be empty. Please try again.")

    status_options = ["Applied", "Rejected"]

    print("Select application status:")
    for i, status in enumerate(status_options):
        print(f"{i + 1}. {status}")

    while True:
        try:
            status_choice = int(input("Enter the number corresponding to the status: "))
            if 1 <= status_choice <= len(status_options):
                status = status_options[status_choice - 1]
                break
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    notes = input("Enter any notes (optional): ")
    return [formatted_date, company, position, status, notes]  # Use formatted date

def write_to_google_sheets(details):
    data = {
        "values": [details]
    }
    try:
        result = service.spreadsheets().values().append(
            spreadsheetId=SHEET_ID, range=RANGE,
            valueInputOption='RAW', body=data).execute()

        if result.get('updates').get('updatedCells') > 0:
            print("Application details saved to Google Sheets.")
        else:
            print("Error: Could not write to sheet. Check permissions and sheet configuration.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        details = get_application_details()
        write_to_google_sheets(details)

        while True:
            add_another = input("Add another application? (1 for yes, 2 for no): ")
            if add_another == '1':
                break
            elif add_another == '2':
                return
            else:
                print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()