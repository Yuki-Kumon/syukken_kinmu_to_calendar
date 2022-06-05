import argparse

from googleapiclient.discovery import build

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

    args = parser.parse_args()
