import numpy as np

F = 'data/11_diecasting_series.csv'

def col(c):
  return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)

# 실습 1
# cyc = col(0)
# ct = col(1)

# idx = ct.argmax()
# # print(cyc[idx], ct[idx])    # 50.0 6170.0l

# # 실습 2
# cyc = col(0)
# ct = col(1)

# change = np.abs(np.diff(ct))
# j = change.argmax()
# print(int(cyc[j]), int(cyc[j+1]), round(change[j], 1))      # 49 50 6133.9

# 실습 3
# cyl = col(2)
# cyl[0] = 9999
# print(round(cyl.mean(), 1))     # 421.5

# fixed = np.clip(cyl, 100, 300)
# print(round(fixed.mean(), 1))    # 227.5

# # 실습 4
# ct = col(1)
# label = np.where(ct >= 1000, 2, np.where(ct >= 50, 1, 0))

# kinds, count = np.unique(label, return_counts=True)
# print(kinds, count)     # [0 1 2] [46  2  2]
# print(count / count.sum())      # [0.92 0.04 0.04]

# # 실습 5
# M = np.stack([col(1), col(2), col(3), col(4)])
# print(M.shape)

# recent = M[:, -10:]
# print(recent.shape)

# 실습 6
cyc, ct, cyl = col(0), col(1), col(2)

i = ct.argmax()
print(int(cyc[i]), ct[i])                    # 50 6170.0

ch = np.abs(np.diff(ct))
j = ch.argmax()
print(int(cyc[j]), int(cyc[j+1]))           # 49 50

warn = np.where((ct >= 50) | (cyl < 150), 1, 0)
print(round(warn.mean(), 2))      # 0.12

top = np.argsort(ct)[::-1][:3]
print(top)      # [49 47 42]  -> 인덱스
print(cyc[top])   # [50. 48. 43.]