"""
convertedData = {
    'date': '2022-06-01',
    'type': 0,  # 0:休日, 1:出勤, 2: 早出出勤, 99: エラー
    'title': '出勤(8:50〜)',
    'remark': '編成・作業: W0\n特記事項: A構内試運転',
}

#A 休日、出勤日ごとに別のリストで出力
output = {
    'summary': '早出(8:20〜)',
    'description': '早出のため出勤時刻に注意！\n編成・作業: W0\n特記事項: A構内試運転',
    'start': {
        # 'dateTime': '2022-06-01T00:00:00',
        'date': '2022-06-01',
        'timeZone': 'Japan',
    },
    'end': {
        'date': '2022-06-01',
        'timeZone': 'Japan',
    },
}
"""


def dataToCalendarEvent(convertedData):
    weekdayList = []
    earlydayList = []
    holidayList = []
    for data in convertedData:
        eventData = {
            'summary': data['title'],
            'description': data['remark'],
            'start': {
                'date': data['date'],
                'timeZone': 'Japan',
            },
            'end': {
                'date': data['date'],
                'timeZone': 'Japan',
            },
        }
        if data['type'] == 0:
            holidayList.append(eventData)
        elif data['type'] == 1:
            weekdayList.append(eventData)
        elif data['type'] == 2:
            earlydayList.append(eventData)
        else:
            # 暫定処置
            weekdayList.append(eventData)

    return weekdayList, earlydayList, holidayList


if __name__ == '__main__':
    from loadCsv import loadCsv
    from convertData import convertData
    dataToCalendarEvent(convertData(*loadCsv('./data/2022年6月.csv', dataLineEnd=32)))
