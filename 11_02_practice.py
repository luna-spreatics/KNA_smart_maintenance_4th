import numpy as np

F = 'data/11_hydraulic_cooler.csv'

def col(c):
  return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)


# 실습 1
vib = col(2)

# print(np.isnan(vib).sum())  # 6
# print(round(np.isnan(vib).mean(), 2))   # 0.12
# print(round(np.nanmean(vib), 3))    # 0.566
# print(np.mean(vib))   # nan


# 실습 2
temp = col(1)
q1, q3 = np.percentile(temp, [25, 75])
upper = q3 + 1.5 * (q3 - q1)    # 상한값
print(temp[temp > upper])   # 상한 초과
print(int((temp > upper).sum()))

# 실습 3
cyc = col(0)
temp = col(1)

# 표준화
z = (temp - np.nanmean(temp)) / np.nanstd(temp)
abnormal = np.abs(z) > 2
print(cyc[abnormal].astype(int))      # [47 48 49 50]
print(round(np.abs(z).max(), 2))    # 3.39

# 실습 4
cyc = col(0)
temp = col(1)

high = np.nanmean(temp) + 3 * np.nanstd(temp)
print(round(high, 2))
print(cyc[temp > high].astype(int))

# 실습 5
temp = col(1)
ce = col(3)

corr = np.corrcoef(temp, ce)
print(round(corr[0, 1], 2))     # -0.99

# 실습 6
M = np.stack([col(1), col(2), col(3), col(4)])
print(M.shape)  # (4, 50)
print(np.round(np.nanmean(M, axis = 1), 1))     # [37.7  0.6 44.7 57.7]
print(np.round(np.nanstd(M, axis = 1), 1))       # [6.  0.1 7.6 1.6]

# 실습 7
cyc = col(0)
temp = col(1)

cs = np.cumsum(temp - np.nanmean(temp))
k = np.argmin(cs)
print(int(cyc[k]), round(cs[k], 1))     # 45 -81.7


# 실습 8
cyc = col(0)  # 사이클 번호
t = col(1)    # 온도
ce = col(3)   # 냉각효율
st = col(5)   # 상태 라벨

# z-score 절댓값 구하기
def z(a):
  return np.abs((a - np.nanmean(a)) / np.nanstd(a))

score = z(t) + z(ce)

i = np.nanargmax(score)

print(int(cyc[i]), round(score[i], 2))

# 상위 세 시점
top = np.argsort(score)[::-1][:3]
print(cyc[top].astype(int))

