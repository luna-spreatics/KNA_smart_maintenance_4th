# 실습 1
# s1 = ("모터온도", 78)
# print(s1)     # ('모터온도', 78)
# print(s1[0], s1[1])
# name, value = s1
# print(name, value)

# 실습 2
sensors = [("모터온도", 78), ("회전속도", 1750), ("펌프압력", 95), ("유량", 42)]
for name, value in sensors:
    # print(name, value)
    if value > 90:
        print(name, "경고")


# 실습 3
sensors = [
    ("모터온도", 78, (3, 5)),
    ("베어링진동", 0.5, (7, 2)),
    ("펌프압력", 95, (4, 8)),
]
for name, value, pos in sensors:
    x, y = pos
    print(name, "위치:", x, y)
    if x <= 5:
        print(name)
