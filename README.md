# syukken_kinmu_to_calendar
## APIの使用について
[こちら](https://www.coppla-note.net/posts/tutorial/google-calendar-api/)を参考に、google calendar apiを有効にし、oauthクライアントを作成する。client secret情報のjsonファイルを`./secret`に保存する。

calendar_idについて、`./secret`に以下のフォーマットで保存。
```
{
  "syukkin": {
    "calendar_id": "hoge@group.calendar.google.com"
  },
  "hayade": {
    "calendar_id": "huga@group.calendar.google.com"
  },
  "kyuuzitsu": {
    "calendar_id": "ngo@group.calendar.google.com"
  }
}
```

## 勤務表excelファイルからの読み込み設定について
`insertFromExcel.py`の引数で設定。

|引数|説明|
|:-|:-|
|dateEnd|月の日数|
|userRowStart|勤務表で自分の勤務が何行目から記載されているか(一番上の行を0行目として数える)。|

実行例
```
python insertFromExcel.py --dateEnd 30 --userRowStart 35
```
