from __future__ import print_function
from datetime import datetime, timedelta, timezone
import os.path
from googleapiclient.discovery import Resource, build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def authenticate () -> Credentials :
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        return creds
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
        
        return creds

def _getUpcomingEvents (service : Resource) : 

    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
 

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

def createDateTimeISTtoGMT () :
    IST = timezone(timedelta(hours=5, minutes=30))
    UTC = timezone.utc
    currentYear = datetime.utcnow().year
    startTime = datetime(currentYear, 9, 18, hour=12, minute=12, tzinfo = IST).astimezone(UTC)
    endTime = datetime(currentYear, 9, 18, hour=22, minute=12, tzinfo = IST ).astimezone(UTC)
    startTime.weekday

def main():  

    service = build('calendar', 'v3', credentials=authenticate())

    _getUpcomingEvents(service)
    IST = timezone(timedelta(hours=5, minutes=30))
    UTC = timezone.utc
    currentYear = datetime.utcnow().year
    startTime = datetime(currentYear, 9, 18, hour=12, minute=12, tzinfo = IST).astimezone(UTC)
    endTime = datetime(currentYear, 9, 18, hour=22, minute=12, tzinfo = IST ).astimezone(UTC)

    event = {
        'summary': 'Appointment',
        'location': '',
        'start': {
            'dateTime': startTime.isoformat(),
            'timeZone': 'UTC'
        },
        'end': {
            'dateTime': endTime.isoformat(),
            'timeZone': 'UTC'
        },
        'recurrence': [
            'RRULE:FREQ=WEEKLY;UNTIL=20220701T170000Z',
        ],
        'attendees': [
            {
            'email': 'attendeeEmail@gmail.com',
            # Other attendee's data...
            },
            # ...
        ],
    }

    # event = service.events().insert(calendarId='primary', body=event).execute()
    # print ('Event created: %s' % (event.get('htmlLink')))

    calendar = {
    'summary': 'Contacts',
    'timeZone': 'America/Los_Angeles'
    }

    created_calendar = service.calendars().insert(body=calendar).execute()

    print(created_calendar['id'])




if __name__ == '__main__':
    main()