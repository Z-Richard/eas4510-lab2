# EAS 4510 Synoptic Meteorology Lab 2

### Some rough guidance on this repository
- `main.py` is the Python file used to calculate the skill scores for the dataset.
- `download_mos.py` is used to download the MOS data. Note that at line 8 one can change the station ID to experiment with different stations.
- `nbm.py` is used to download the national blend of models (NBM) data. Note that at line 22 one can change the station ID to experiment with different stations.
- `nbm_kfnl.csv`, `mos.csv` contain data collected from `download_mos.py` and `nbm.py`.
- `obs_kfnl.csv` is collected manually.
- To run the code on a server to download data automatically, run `nohup python mos.py >& mos.log &`, where `mos.log` is used to output the error message.