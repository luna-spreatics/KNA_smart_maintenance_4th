import numpy as np

# 실습 1
# rpm = np.array([4603, 4603, 58, 4603, 4603,
#                 1216, 4603, 4603, 1217, 4603])
# print(rpm[0], rpm[-1])
# print(rpm[1:4])
# print(rpm[::2])

# # 실습 2
# data = np.array([[4603, 2], [58, 5],
#                  [1216, 1], [4967, 21]])
# print(data[2])
# print(data[:, 0])
# print(data[:, 1])

# # 실습 3
# rpm = np.array([4603, 4603, 58, 4603, 4603,
#                 1216, 4603, 4603, 1217, 4603])

# norm = (rpm - rpm.min()) / (rpm.max() - rpm.min())
# print(np.round(norm, 2))

# 실습 4
rpm = np.array([4603, 4603, 58, 4603, 4603,
                1216, 4603, 4603, 1217, 4603])
# 전류 데이터 (실습용 예시값)
current = np.array([2, 2, 21, 2, 3,
                    2, 2, 3, 2, 147])
data = np.array([[4603, 2], [4603, 21]])


low_rpm = rpm < 2000
# 회전수 2000 미만
print(rpm[low_rpm])
# 회전수 2000 미만 또는 전류 25 초과
print(rpm[low_rpm], current[current> 25])

# 개수
print(np.sum(low_rpm))
print(np.sum((rpm < 2000) | (current > 25)))

# 비율
print(np.mean(low_rpm) * 100, "%")
# - low_rpm : True False 배열 -> True: 1, False: 0
print(np.mean((rpm < 2000) | (current > 25))* 100, "%")

# 실습 5
tq = np.array([2, 2, 21, 2, 3, 2, 2, 3, 2, 147])
high = tq > 10
print(high.sum())   # 2
print(round(high.mean(), 2))    # 0.2


# 실습 6
# 4시점 × 2센서(회전수, 토크) — 실측값
data = np.array([[4603, 2], [4967, 21],
                 [3632, 147], [58, 5]])

print(np.round(data.mean(axis=0), 1))
print(np.round(data.std(axis=0), 1))


# 실습 7
rpm = np.loadtxt('data/10_mct_tool.csv',
                 delimiter=",",      # 값을 나누는 기호
                 skiprows=1,        # 첫 줄(제목)은 건너뜀
                 usecols=4) 

print(round(rpm.mean(), 1))
print(round(rpm.std(), 1))
print(rpm.min(), rpm.max())

# 실습 8
tq = np.loadtxt('data/10_mct_tool.csv',
                 delimiter=",",      # 값을 나누는 기호
                 skiprows=1,        # 첫 줄(제목)은 건너뜀
                 usecols=5) 

high = tq[tq > 10]
print(np.round(high, 1))
print(high.size, round(high.mean(), 1))

# 실습 9
rpm_tq = np.loadtxt('data/10_mct_tool.csv',
                 delimiter=",",      # 값을 나누는 기호
                 skiprows=1,        # 첫 줄(제목)은 건너뜀
                 usecols=(4,5))  

rpm = rpm_tq[:, 0]
print(rpm_tq.shape, rpm_tq.dtype)
low = rpm[rpm < 2000]
print(low.size, round(low.mean(), 1))
print(round(rpm.mean(), 1))