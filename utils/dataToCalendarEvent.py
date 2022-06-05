"""
#A 休日、出勤日ごとに別のリストで出力
output = {
    'summary': 早出(8:20〜)',
    'description': '早出のため出勤時刻に注意！\n編成・作業: W0\n特記事項: A構内試運転',
    'start': {
        'dateTime': '2022-06-01',
        'timeZone': 'Japan',
    },
    'end': {
        'dateTime': '2022-06-01',
        'timeZone': 'Japan',
    },
}
"""


def dataToCalendarEvent(convertedData):
    print(convertedData)


if __name__ == '__main__':
    from loadCsv import loadCsv
    from convertData import convertData
    dataToCalendarEvent(convertData(*loadCsv('./data/2022年6月.csv', dataLineEnd=32)))
