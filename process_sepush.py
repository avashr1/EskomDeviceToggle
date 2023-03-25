import json
from datetime import datetime as dt
from datetime import timedelta
from TCL_TV_ON import tv_toggle

f = open('json_data.json')

data = json.load(f)
s = data

for i in (s['events']):
    raw = i['end']
    w_date = raw[0:raw.find("T")]
    now = dt.now()
    now_date = now.strftime("%Y-%m-%d")
    w_time = raw[raw.find("T") + 1:raw.find("+")]

    if w_date == now_date:

        now_time = dt.now() - timedelta(minutes=15)
        now_time = now_time.strftime("%H:%M:%S")
        f3 = open('Time.txt')
        w_pre_time = f3.read()
        f3.close()
        f4 = open('Date.txt')
        w_pre_date = f4.read()
        f4.close()
        if now_date == w_pre_date:
           if (now_time > w_time) & (w_time != w_pre_time):

            tv_toggle()
            f2 = open('Time.txt', 'w')
            f2.write(w_time)
            f2.close()
        else:
            if now_time > w_time :
                tv_toggle()
                f5 = open('Time.txt', 'w')
                f5.write(w_time)
                f5.close()
                f6 = open('Date.txt', 'w')
                f6.write(w_date)
                f6.close()
f.close()
