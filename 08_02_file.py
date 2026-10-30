import os
import csv


# 파일 입출력
# open()
# 형식: open(파일명, 모드, encoding)
# - 모드: r=읽기, w=새로쓰기, a=이어쓰기
# - encoding = "utf-8" => 한글이 깨지지 않도록 하는 것

FILE = "data/08_press.csv"

# f = open(FILE, "r", encoding="utf-8")
# text = f.read()
# print(text)
# f.close()       # 파일을 열고 난 후 닫기까지

# f = open(FILE, "r", encoding="utf-8")
# lines = f.readlines()
# print(type(lines), len(lines))      # <class 'list'> 13
# f.close()       # 파일을 열고 난 후 닫기까지


# # with open - 블록이 끝나면 자동 닫힘
# with open(FILE, "r", encoding="utf-8") as f:
#     for line in f:
#         print(line)

# # write()
# with open("data/test.txt", "w", encoding="utf-8") as f:
#     f.write("쓰기 테스트")


# 실습 2
# with open("data/test.txt", "w", encoding="utf-8") as f:
#     f.write("쓰기 테스트\n")
#     f.write("이상 없음\n")
# with open("data/test.txt", "r", encoding="utf-8") as f:
#     print(f.read())

# # 실습 3
# with open("data/08_log.txt", "w", encoding="utf-8") as f:
#     f.write("1차 점검\n")
# with open("data/08_log.txt", "a", encoding="utf-8") as f:
#     f.write("추가 점검\n")       # a = 기존 내용 뒤에 이어 붙임
# with open("data/08_log.txt", "r", encoding="utf-8") as f:
#     print(f.read())


# csv.reader
# with open(FILE, "r", encoding="utf-8") as f:
#   reader = csv.reader(f)
#   for row in reader:
#     print(row)


# csv.writer
with open("data/08_summary.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["설비ID", "상태"])     # 헤더
    writer.writerow(["PRESS-01", 1])
    writer.writerow(["PRESS-02", 1])

with open("data/08_summary.csv", "r", encoding="utf-8") as f:
    print(f.read())
