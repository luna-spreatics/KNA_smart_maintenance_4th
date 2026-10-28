# 실습 1
# s1 = ("모터온도", 78)
# print(s1)     # ('모터온도', 78)
# print(s1[0], s1[1])
# name, value = s1
# print(name, value)

# 실습 2
# sensors = [("모터온도", 78), ("회전속도", 1750), ("펌프압력", 95), ("유량", 42)]
# for name, value in sensors:
#     # print(name, value)
#     if value > 90:
#         print(name, "경고")


# # 실습 3
# sensors = [
#     ("모터온도", 78, (3, 5)),
#     ("베어링진동", 0.5, (7, 2)),
#     ("펌프압력", 95, (4, 8)),
# ]
# for name, value, pos in sensors:
#     x, y = pos
#     print(name, "위치:", x, y)
#     if x <= 5:
#         print(name)

# 실습 4
logs = ["S01", "S02", "S01", "S03", "S02"]
unique_logs = set(logs)
print(sorted(unique_logs))
print("종류 수:", len(unique_logs))

# 실습 5
line_a = {"S01", "S02", "S03", "S05"}
line_b = {"S03", "S04", "S05"}
print(line_a.union(line_b))         # 전체
print(line_a.intersection(line_b))  # {'S03', 'S05'}
print(line_a.difference(line_b))    # {'S01', 'S02'}
print(line_b.difference(line_a))    # {'S04'}


# 실습 6
yesterday = {"S01", "S02", "S03"}
today = {"S02", "S03", "S05"}
print(today.difference(yesterday))    # 신규: {'S05'}
print(today.intersection(yesterday))  # 지속: {'S02', 'S03'}

