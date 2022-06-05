import io
import pandas as pd
import datetime

from utils.loadCsv import loadCsv
# from loadCsv import loadCsv


def serialToDateTime(serialVal):
    """日付シリアル値からyyyy/MM/dd HH:MM:ss 形式に変換
    Args:
        serialVal (float): シリアル値(Ex: 44434.3412172569)
    Returns:
        str: 時刻  yyyy/MM/dd HH:MM:ss 形式
    参考: https://qiita.com/Yusuke_Pipipi/items/5227bd8187a584ac391b
    """
    try:
        sDateTime = (datetime.datetime(1899, 12, 30) + datetime.timedelta(serialVal)).strftime('%m月%d日')
    except:
        sDateTime = ''

    return sDateTime


def loadExcel(excelFile='./data/2022_6.xlsx', userRowStart=35, dateLine=0, dataLineStart=3, dataLineEnd=33, year=2022):
    csv_stream = io.StringIO()
    df = pd.read_excel(excelFile, header=None)  # 1枚目のシートを読み込む
    # excelのシリアル値を日付に変更
    df.iloc[dateLine] = df.iloc[dateLine].apply(serialToDateTime)
    df.to_csv(csv_stream, index=False, header=False)
    csv_stream.seek(0)

    return loadCsv(csv_stream, userRowStart, dateLine, dataLineStart, dataLineEnd, year, True)


if __name__ == '__main__':
    loadExcel()
