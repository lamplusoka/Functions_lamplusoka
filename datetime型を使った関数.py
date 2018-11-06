import datetime

#文字列の日付をdatetime型へ変換→一日足す→文字列の日付へ変換
def get_time_next(time_given_string):
    time_given_datetime = datetime.datetime.strptime(time_given_string, '%Y/%m/%d') #日付文字列をdatetimeへ変換
    time_add_day_one    = time_given_datetime + datetime.timedelta(days=1) #一日足す
    time_next_day       = f'{time_add_day_one:%Y/%m/%d}' #time_add_day_one.strftime('%Y/%m/%d') #日付を文字列へ変換
    return time_next_day

#日付から曜日を割り出す
def get_weekday(time_given_string):
    weekday = ['月', '火', '水', '木', '金', '土','日']
    time_given_datetime = datetime.datetime.strptime(time_given_string, '%Y/%m/%d') #日付文字列をdatetimeへ変換
    time_weekday_number = time_given_datetime.weekday() #曜日の値を取得
    time_weekday        = weekday[time_weekday_number] #曜日の値→文字列で曜日へ
    return time_weekday