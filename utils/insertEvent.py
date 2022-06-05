def insertEvent(service, calendarId, eventList):
    for event in eventList:
        _ = service.events().insert(calendarId=calendarId, body=event).execute()


if __name__ == '__main__':
    from googleapiclient.discovery import build
    from getCredentials import getCredentials
    creds = getCredentials(clientSecretPass='./secret/client_secret_508123958036-57icko740m45opd0utd92891n07p0iqe.apps.googleusercontent.com.json', save=False)
    service = build('calendar', 'v3', credentials=creds)

    body = {
        'summary': '早出(8:20〜)',
        'description': '早出のため出勤時刻に注意！\n編成・作業: W0\n特記事項: A構内試運転',
        'start': {
            'date': '2022-06-06',
            'timeZone': 'Japan',
        },
        'end': {
            'date': '2022-06-06',
            'timeZone': 'Japan',
        },
    }

    event = service.events().insert(calendarId='j61u07m2kjgasi1kr0d3d1j1dg@group.calendar.google.com', body=body).execute()
