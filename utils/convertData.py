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
        '年': 5,
    },
    'description': {
        0: '出勤(8:50〜)',
        1: '早出(8:20〜)',
        2: '特休',
        3: '公休',
        4: '一時帰休',
        5: '年休',
        99: 'エラー！勤務表を要確認！',
    },
    'type': {
        0: [2, 3, 4, 5],
        1: [0],
        2: [1],
    },
    'remark': {
        '前': '前作業',
        '本': '本線試運転',
        'A': 'A構内試運転',
        'B': 'B構内試運転',
        'C': 'C構内試運転'
    },
}


def convertWork(work_input, idx):
    work_text = ''
    flag = False

    if work_input[0][idx]:
        flag = True
        work_text += '搭載品降ろし(早出): ' + work_input[0][idx] + '\n'
    if work_input[1][idx] or work_input[2][idx]:
        flag = True
        work_text += '前作業: '
        if work_input[1][idx]:
            work_text += work_input[1][idx]
        elif work_input[2][idx]:
            work_text += work_input[2][idx]
        if work_input[2][idx]:
            work_text += '・' + work_input[2][idx]
        work_text += '\n'
    if work_input[3][idx]:
        flag = True
        work_text += '臨時作業・仕業検査: ' + work_input[3][idx] + '\n'
    if work_input[4][idx]:
        flag = True
        work_text += 'A構内試運転: ' + work_input[4][idx] + '\n'
    if work_input[5][idx]:
        flag = True
        work_text += 'B構内試運転: ' + work_input[5][idx] + '\n'
    if work_input[6][idx]:
        flag = True
        work_text += 'C構内試運転: ' + work_input[6][idx] + '\n'
    if work_input[7][idx]:
        flag = True
        work_text += '本線試運転(西行き・6793): ' + work_input[7][idx] + '\n'
    if work_input[8][idx]:
        flag = True
        work_text += '本線試運転(東行き・6778): ' + work_input[8][idx] + '\n'
    if work_input[9][idx]:
        flag = True
        work_text += '本線試運転(6795): ' + work_input[9][idx] + '\n'

    if flag:
        return '\n【作業予定】\n' + work_text
    else:
        return ''


def convertData(user_input, work_input, date_input):
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
        remark_text += convertWork(work_input, idx)
        output.append({
            'date': datetime.datetime.strptime(date_row, '%Y年%m月%d日').strftime('%Y-%m-%d'),
            'type': 0 if event_type in CONVERT_RULE['type'][0] else 1 if event_type in CONVERT_RULE['type'][1] else 2 if event_type in CONVERT_RULE['type'][2] else event_type,
            'title': CONVERT_RULE['description'].get(event_type),
            'remark': remark_text,
        })

    return output


if __name__ == '__main__':
    from loadCsv import loadCsv
    convertData(*loadCsv('./data/2022年6月.csv', dataLineEnd=32))
