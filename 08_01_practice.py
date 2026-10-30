import os
import datetime

# 실습 3
print(os.getcwd())      # 현재 작업 폴더
files = os.listdir("data")
for file in files:
    print(file)

print("=========")
for file in files:
    if file.endswith(".csv"):
        print(file)


# 실습 4
path = os.path.join("data", "08_press.csv")
print(os.path.exists(path))   # True

if os.path.exists(path):
    print("파일 있음")
else:
    print("파일 없음")


# 실습 5
files = os.listdir("data")
now = datetime.datetime.now()
print(f'파일 {len(files)}개, 점검 시작 {now}')

# 실습 6
files = os.listdir("data")
csvs = []
for n in files:
    if n.endswith(".csv"):
        csvs.append(n)

print("[CSV]")
for n in csvs:
    path = os.path.join("data", n)
    print(" -", path)
