import argparse
import json

from googleapiclient.discovery import build

from utils.getCredentials import getCredentials
from utils.loadCsv import loadCsv
from utils.convertData import convertData
from utils.dataToCalendarEvent import dataToCalendarEvent
from utils.insertEvent import insertEvent


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--csv', default='./data/2022年6月.csv')
    parser.add_argument('--calendarId', default='./secret/calendar.json')
    parser.add_argument('--clientSecret', default='./secret/client_secret_508123958036-57icko740m45opd0utd92891n07p0iqe.apps.googleusercontent.com.json')
    parser.add_argument('--token', default='./secret/accessToken.json')
    parser.add_argument('--dateEnd', type=int, default=31)  # 月の最終日
    parser.add_argument('--userRowStart', type=int, default=35)

    args = parser.parse_args()

    # calendarIdの取得
    with open(args.calendarId, 'r') as f:
        calendarIdDict = json.load(f)

    # イベントのリストの作成
    dataLineEnd = args.dateEnd + 2
    weekdayList, earlydayList, holidayList = dataToCalendarEvent(convertData(*loadCsv(csvFile=args.csv, dataLineEnd=dataLineEnd, userRowStart=args.userRowStart)))

    # googlecalendarのserviceの取得
    creds = getCredentials(clientSecretPass=args.clientSecret, tokenPass=args.token)
    service = build('calendar', 'v3', credentials=creds)

    # イベントの登録
    insertEvent(service, calendarIdDict['syukkin']['calendar_id'], weekdayList)
    insertEvent(service, calendarIdDict['hayade']['calendar_id'], earlydayList)
    insertEvent(service, calendarIdDict['kyuuzitsu']['calendar_id'], holidayList)
