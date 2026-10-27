# 실습 1
# temps = [25, 32, 28, 35, 19, 31, 27]
# for t in temps:
#     if t >= 30:
#         print("고온:", t)

# # 실습 2
# hours = [3, 8, 12, 6, 10, 4, 9]
# for h in hours:
#     if h >= 5 and h <= 10:
#         print(h)


# # 최대, 최소
# temps = [25, 32, 28, 36, 27, 31]
# biggest = temps[0]
# for t in temps:
#     if t > biggest:
#         biggest = t    # 더 큰값일 때 갱신
# print(biggest)


# # 빈 리스트 채우기
# doubled = []
# for t in temps:
#   doubled.append(t * 2)
# print(doubled)        # [50, 64, 56, 72, 54, 62]

# 실습 3
temps = [25, 32, 28, 36, 27, 31, 24]
total = 0
count = 0
for t in temps:
  if t > 30:
    total += t
    count += 1
print("고온 평균:", total/count)


# 실습 4
temps = [25, 32, 28, 35, 27, 31, 24, 33]
hot = []
for t in temps:
  if t > 30:
    hot.append(t)
print(hot)
print(len(hot))

# 실습 5
temps = [25, 26, 24, 28, 27]
fahrenheit = []
for t in temps:
  fahrenheit.append(t * 1.8 + 32)
print(fahrenheit)

# 중첩 리스트 - 리스트 안에 리스트
# - 표(행,열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행', 안쪽 인덱스로 '열'
rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
for row in rows:
  print(row[0], "온도", row[1])
  
  
# 실습 6
temps = [25, 32, 28, 35, 27, 31, 24, 33, 29, 36]
total = 0
hot = []
for t in temps:
  total += t
  
  if t > 30:
    hot.append(t)
  
hot_total = 0
for h in hot:
  hot_total += h
print("전체 평균:", total / len(temps))
print("고온 평균:", hot_total / len(hot))
