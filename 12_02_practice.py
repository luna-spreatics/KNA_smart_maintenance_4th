import pandas as pd
import numpy as np

F = 'data/12_metro_compressor.csv'
FD = 'data/12_metro_digital.csv'
# 실습 2
# df = pd.read_csv(FD)
# print(df.shape)
# print(df.columns.tolist())
# print(df.dtypes)
# print(df.head())

# 실습 3
# df = pd.read_csv(F)
# print(df.info())
# 오일온도 -> 199 -> 결측 1개

# 실습 4
# df = pd.read_csv(F)
# print(df.describe().round(2))

# # 두 열을 배열로 꺼내 상태별로 나눠 확인
# state = df["가동상태"].values
# cur = df["모터전류"].values

# print(round(float(np.mean(cur[state == "가동"])), 2))   # 4.25
# print(round(float(np.mean(cur[state == "정지"])), 2))   # 0.04

# 실습 6
FS = 'data/12_metro_small.csv'
df = pd.read_csv(FS)
print(df.head(3))
print('크기:', df.shape)
print(df.info())

stats = df.describe()

miss = int(df["오일온도"].isna().sum())
print('오일온도 결측:', miss, '건')

mean_current = round(float(stats["모터전류"]["mean"]), 2)
median_current = round(float(stats["모터전류"]["50%"]), 2)
print("모터전류 평균/중앙값:", mean_current, median_current)