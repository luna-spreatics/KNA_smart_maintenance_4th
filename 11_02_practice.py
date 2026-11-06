import numpy as np

F = 'data/11_hydraulic_cooler.csv'

def col(c):
  return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)


# 실습 1
vib = col(2)

print(np.isnan(vib).sum())  # 6
print(round(np.isnan(vib).mean(), 2))   # 0.12
print(round(np.nanmean(vib), 3))    # 0.566
print(np.mean(vib))   # nan