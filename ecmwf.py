from herbie.archive import Herbie

H = Herbie('2022-08-30', model='ecmwf', product='oper', fxx=12)
H.download()
