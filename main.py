import numpy as np
import pandas as pd
from datetime import timedelta

mos = pd.read_csv('mos.csv', names=[
                  'date', 'mos_d1min', 'mos_d2max', 'mos_d2min'])
nbm = pd.read_csv('nbm_kfnl.csv', names=[
                  'date', 'nbm_d1min', 'nbm_d2max', 'nbm_d2min'])
df = mos.merge(nbm, left_on='date', right_on='date')
df['date'] = pd.to_datetime(df['date'])

obs = pd.read_csv('obs_kfnl.csv')
obs.columns = ['date', 'max_temp', 'min_temp',
               '1', '2', '3', '4', '5', '6', '7']
obs.drop(columns=[str(i+1) for i in range(7)], inplace=True)
obs['date'] = pd.to_datetime(obs['date'])

start_date, end_date = df.loc[0, 'date'], df.loc[len(df) - 1, 'date']
df['obs_d1min'] = obs.loc[(obs['date'] >= start_date + timedelta(days=1))
                          & (obs['date'] <= end_date + timedelta(days=1)), 'min_temp'].tolist()
df['obs_d2max'] = obs.loc[(obs['date'] >= start_date + timedelta(days=2))
                          & (obs['date'] <= end_date + timedelta(days=2)), 'max_temp'].tolist()
df['obs_d2min'] = obs.loc[(obs['date'] >= start_date + timedelta(days=2))
                          & (obs['date'] <= end_date + timedelta(days=2)), 'min_temp'].tolist()

df = df.replace(' M', np.nan).dropna()
df = df.apply(lambda x: pd.to_numeric(x.str.strip())
              if x.dtype == "object" else x)
print(df)

d1min_score = 1 - np.sum(np.abs(df['nbm_d1min'] - df['obs_d1min'])) / \
    np.sum(np.abs(df['mos_d1min'] - df['obs_d1min']))
d2max_score = 1 - np.sum(np.abs(df['nbm_d2max'] - df['obs_d2max'])) / \
    np.sum(np.abs(df['mos_d2max'] - df['obs_d2max']))
d2min_score = 1 - np.sum(np.abs(df['nbm_d2min'] - df['obs_d2min'])) / \
    np.sum(np.abs(df['mos_d2min'] - df['obs_d2min']))

d1min_score *= 100
d2max_score *= 100
d2min_score *= 100

print(d1min_score, d2max_score, d2min_score)
