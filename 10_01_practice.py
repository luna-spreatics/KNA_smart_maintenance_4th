import numpy as np

# 실습 1
temp = np.array([30, 30, 30, 30, 29, 30])
print("측정 온도:", temp)
print("화씨:", temp * 1.8 + 32)

# 실습 2
scale = np.linspace(0, 70, 8)
print(scale)

# 실습 3
idx = np.arange(0, 40, 5)
print(idx)

# 실습 4
# 4시점 × 2센서(온도, 전류)
data = np.array([[30, 15.44], [30, 18.69],
                 [30, 62.48], [30, 18.37]])
print(data.ndim)
print(data.shape)
print(data.size)

# 실습 5

# 전류 4회 측정 (실측값)
amp = np.array([15.44, 18.69, 62.48, 18.37])
print(amp.dtype)    # float64
cut = amp.astype(int)
print(cut)    # 


# 실습 6
# 사이클타임 12회 측정 (실측값)
ct = np.array([21156, 15611, 15633, 15601,
               15607, 15557, 15557, 15636,
               15600, 15634, 21207, 15554])
print(ct.reshape(3, 4))


# 실습 7
# 4시점 × 3센서(온도, 전류, 회전수)를 한 줄로 이어 놓은 상태
flat = np.array([30, 15.44, 4603, 30, 18.69, 4603,
                 30, 62.48, 4967, 30, 18.37, 4603])

table = flat.reshape(4, 3)
print(table)
print(table.flatten())
