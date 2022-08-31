from ftplib import FTP
from datetime import datetime
import schedule
import time


def nbm():
    ftp = FTP(
        'ftp.ncep.noaa.gov')
    ftp.login()
    time = datetime.now().strftime('%Y%m%d')

    ftp.cwd(f'/pub/data/nccf/com/blend/prod/blend.{time}/13/text/')

    with open('nbm.txt', 'wb') as fp:
        ftp.retrbinary('RETR blend_nbstx.t13z', fp.write)

    ftp.quit()

    with open('nbm.txt', 'r') as fp:
        data = fp.readlines()
        ind = [i for i, item in enumerate(data) if 'KFNL' in item][0]
        subset = data[ind:ind+10].copy()
        subset = list(map(lambda x: x.strip(), subset))
        nx_line = list(filter(lambda x: x[:3] == 'TXN', subset))[0]
        lhl = nx_line.split()[1:4]
        time = datetime.now().strftime('%Y-%m-%d')
        lhl = [time] + lhl

        with open('nbm_kfnl.csv', 'a') as f:
            f.write(','.join(lhl))
            f.write('\n')


schedule.every().day.at('16:00').do(nbm)

while True:
    schedule.run_pending()
    time.sleep(1)
