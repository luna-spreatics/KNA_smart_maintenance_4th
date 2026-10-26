# 리스트
# 형식: 이름 = [값1, 값2, ...]
# - 리스트는 여러 값을 '순서대로' 한 이름에 담는다.

temps = [25, 26, 24, 28, 27]    # 숫자 리스트
machines = ["펌프", "모터", "압축기"]
mixed = ["펌프", 87, True]    # 종류가 달라도 한 리스트에 담을 수 있음

print(len(temps))     # 5
print(len([]))        # 0


# 값 바꾸기 / in 존재 확인
# 형식: 리스트[번호] = 새 값 / 값 in 리스트
nums = [25, 26, 24, 28, 27]
nums[2] = 99
print(nums)       # [25, 26, 99, 28, 27]
print("모터" in machines)


# 값 추가 - append, insert, extend
# 형식: 리스트.append(값) / 리스트.insert(위치, 값) / 리스트.extend(다른 리스트)
data = [25, 26, 24]
data.append(28)       # [25, 26, 24, 28]
data.insert(1, 99)    # [25, 99, 26, 24, 28]
data.extend([30, 31])  # [25, 99, 26, 24, 28, 30, 31]
print(data)

# 값 삭제 - remove, pop, del
# 형식: 리스트.remove(값) / 꺼낸 값 = 리스트.pop(위치) / del 리스트[위치]
d = [25, 26, 24, 28, 27]
d.remove(24)
print(d)        # [25, 26, 28, 27]
got = d.pop(1)
print(got, d)   # 26 [25, 28, 27]
del d[0]
print(d)        # [28, 27]


# 정렬, 탐색 - sort, reverse / count, index
# 형식: 리스트.sort()  .reverse()  .count(값)   .index(값)
l = [27, 24, 30, 22, 26]
# l.sort()      # [22, 24, 26, 27, 30]
# l.sort(reverse=True)    # [30, 27, 26, 24, 22]
l.reverse()      # [26, 22, 30, 24, 27]
print(l)

r = ["정상", "이상", "정상", "정상", "이상"]
print(r.count("정상"), r.index("이상"))     # 3 1
