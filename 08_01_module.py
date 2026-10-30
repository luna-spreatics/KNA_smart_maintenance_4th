# 모듈 / 패키지 / 라이브러리
# - 모듈: 기능을 모아둔 .py 파일 하나
# - 패키지: 모듈을 모아둔 폴더
# - 라이브러리: 위에 사항들을 통칭

# import 방식
# 형식: import 모듈 / from 모듈 import 기능 / import 모듈명 as 별칭
import os
import datetime
import random
import math as m
from math import sqrt, ceil     # 일부만 불러옴 -> 모듈명 없이 바로 사용
import math             # math 라는 모듈을 통째로 불러옴
print(math.sqrt(16))    # 4.0
print(sqrt(16), ceil(4.2))
print(m.sqrt(16))


# 표준 라이브러리 - math / random / datetime
# - 파이썬 설치 시 함께 깔리는 검증된 모듈들

print(random.randint(1, 100))
print(datetime.datetime.now())


# 실습 2
value = random.randint(1, 100)
print(math.sqrt(value))


# ////////////////
# 경로와 os 모듈
# - 파일을 다루려면 어디에 있는지 경로를 알아야 한다
# 1) 절대경로
#   - 최상위부터 전체 주소    ex) C:\Users\user\Desktop\smart_maintenance_4th
# 2) 상대경로
#   - 지금 실행중인 위치를 기준으로 한 주소

print("현재 실행 위치(절대경로):", os.getcwd())

# 폴더 유무 확인
print(os.path.exists("data"))     # True

# 폴더 목록 확인
files = os.listdir("data")
print(files)      # ['08_press.csv']

# 폴더명 + 파일명 -> 경로
path = os.path.join("data", "08_press.csv")

if os.path.exists(path):
    print("파일 경로:", path)
