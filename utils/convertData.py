"""
output = {
    'date': '2022-06-01',
    'type': 0,  # 0:休日, 1:出勤, 2: 早出出勤, 99: エラー
    'title': '出勤(8:50〜)',
    'remark': '編成・作業: W0\n特記事項: A構内試運転',
}
"""


import datetime


CONVERT_RULE = {
    'work': {
        '': 0,
        '早': 1,
        '早出': 1,
        '特': 2,
        '公': 3,
        '帰休': 4,
    },
    'description': {
        0: '出勤(8:50〜)',
        1: '早出(8:20〜)',
        2: '特休',
        3: '公休',
        4: '一時帰休',
        99: 'エラー！勤務表を要確認！',
    },
    'remark': {
        '本': '本線試運転',
        'A': 'A構内試運転',
        'B': 'B構内試運転',
        'C': 'C構内試運転'
    },
}


def convertData(user_input, date_input):
    output = []
    for idx, date_row in enumerate(date_input):
        event_type = CONVERT_RULE['work'].get(user_input[0][idx], 99)  # エラーの際は99を返す
        remark_text = ''
        if event_type == 1:
            remark_text += '早出のため出勤時刻に注意！\n'
        if user_input[1][idx]:
            remark_text += '編成・作業: ' + user_input[1][idx] + '\n'
        if user_input[2][idx]:
            remark_text += '特記事項: ' + CONVERT_RULE['remark'].get(user_input[2][idx], user_input[2][idx]) + '\n'
        else:
            remark_text += '特記事項: 特になし\n'
        output.append({
            'date': datetime.datetime.strptime(date_row, '%Y年%m月%d日').strftime('%Y-%m-%d'),
            'type': 0 if event_type in [2, 3, 4] else 1 if event_type == 0 else 2 if event_type == 1 else event_type,
            'title': CONVERT_RULE['description'].get(event_type),
            'remark': remark_text,
        })

    return output


if __name__ == '__main__':
    from loadCsv import loadCsv
    convertData(*loadCsv('./data/2022年6月.csv', dataLineEnd=32))
