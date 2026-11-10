import pandas as pd

F = 'data/12_metro_compressor.csv'
FS = 'data/12_metro_compressor_semicolon.csv'

# 실습 2
sel = pd.read_csv(F, usecols=["측정시각", "오일온도", "모터전류"])
print(sel.shape)    # (200, 3)

part = pd.read_csv(F, nrows=20)
print(part.shape)   # (20, 7)

# 실습 3
a = pd.read_csv(FS)
print(a.shape)      # (200, 1)

# 값을 나누는 기호를 알려줘서 나눠줘야함
b = pd.read_csv(FS, sep=";", encoding="utf-8")
print(b.shape)      # (200, 7)
print(b.columns.tolist())

# 실습 4
a = pd.read_csv(FS, sep=";", usecols=["측정시각", "오일온도", "모터전류"], nrows=50, encoding="utf-8")
print(a.shape)
print(a.head(50))
