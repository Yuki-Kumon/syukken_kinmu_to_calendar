# from __future__ import print_function
# import datetime
import os.path
# from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


SCOPES = ['https://www.googleapis.com/auth/calendar']


def getCredentials(tokenPass='token.json', clientSecretPass='client_secret,json', save=True):
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(tokenPass):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                clientSecretPass, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        if save:
            with open(tokenPass, 'w') as token:
                token.write(creds.to_json())

    return creds


if __name__ == '__main__':
    import datetime
    from googleapiclient.discovery import build
    # 動作テスト
    creds = getCredentials(clientSecretPass='./secret/client_secret_508123958036-57icko740m45opd0utd92891n07p0iqe.apps.googleusercontent.com.json', save=False)
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='j61u07m2kjgasi1kr0d3d1j1dg@group.calendar.google.com', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
