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
    },
    'remar': {
        '本': '本線試運転',
        'A': 'A構内試運転',
        'B': 'B構内試運転',
        'C': 'C構内試運転'
    },
}


def convertData(user_input, date_input):
    pass
