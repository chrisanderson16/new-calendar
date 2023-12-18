import datetime
import time
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPESX = ["https://www.googleapis.com/auth/calendar.readonly"]


def google_calendar_api(SCOPES):
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.


  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("calendar", "v3", credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    cal_contents = []
    # Prints the start and name of the next 10 events
    #for event in events:
      #start = event["start"].get("dateTime", event["start"].get("date"))
      #print(start, event["summary"])
    
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      cal_contents.append(start)
      cal_contents.append(event["summary"])

  except HttpError as error:
    print(f"An error occurred: {error}")

  return cal_contents

def datetimeformatter(cal_list):
  cal_events = []

  for i in range(0, len(cal_list), 2):
    s = cal_list[i]
    f1 = "%Y-%m-%dT%H:%M:%S%z"
    f2 = "%Y-%m-%d"

    if len(cal_list[i]) > 10:
    #print(len(cal_list[i]))
      out = datetime.datetime.strptime(s, f1).strftime("%b %d @ %-I:%M%p")
    else:
      out = datetime.datetime.strptime(s, f2).strftime("%b %d")
  
    #print(out, cal_list[i+1])
    #print(cal_list[i+1], cal_list[i])

    new = f"{out} {cal_list[i+1]}"
    cal_events.append(new)
  return cal_events




if __name__ == "__main__":
  cal_contents = google_calendar_api(SCOPESX)

  datetimeformatter(cal_contents)