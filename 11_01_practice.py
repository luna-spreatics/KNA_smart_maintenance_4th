import numpy as np

F = 'data/11_diecasting_series.csv'

def col(c):
  return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# 실습 1
cyc = col(0)
ct = col(1)

idx = ct.argmax()
print(cyc[idx], ct[idx])    # 50.0 6170.0