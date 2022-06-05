import csv


def loadCsv(csvFile='./data/kinmu.xlsx', userRowStart=35, dateLine=0, dataLineStart=3, dataLineEnd=33, year=2022):
    # 31日までの月はdateLineEnd=33
    csv_input = []
    with open(csvFile, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            csv_input.append(row)
    # 勤務情報の抜き出し
    user_input = csv_input[userRowStart:userRowStart + 3]
    user_input = [row[dataLineStart:dataLineEnd + 1] for row in user_input]
    # 日付の抜き出し
    date_input = csv_input[dateLine][dataLineStart:dataLineEnd + 1]
    date_input = [str(year) + '年' + row for row in date_input]

    return user_input, date_input


if __name__ == '__main__':
    print(loadCsv('./data/2022年6月.csv', dataLineEnd=32))
