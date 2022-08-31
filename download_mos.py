from urllib.request import urlopen
from datetime import datetime
import schedule
import time


def mos():
    url = 'https://vortex.plymouth.edu/wxp/cgi-bin/fx/gen-mos-text.cgi?id=KFNL&model=GFS'
    data = urlopen(url, timeout=300).read().decode('utf-8')

    nx_line = list(filter(lambda s: s.strip()[:3]
                          in ['N/X', 'X/N'], data.split('\n')))[0]
    nx_split = nx_line.split()
    if nx_split[0] == 'N/X':
        lhl = nx_split[1:4]
    elif nx_split[0] == 'X/N':
        lhl = nx_split[2:5]

    file = 'mos.csv'
    time = datetime.now().strftime('%Y-%m-%d')
    lhl = [time] + lhl

    with open(file, 'a') as f:
        f.write(','.join(lhl))
        f.write('\n')


schedule.every().day.at('15:00').do(mos)

while True:
    schedule.run_pending()
    time.sleep(1)
