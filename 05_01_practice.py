# 실습 1
# n = int(input("끝 숫자 N을 입력하세요: "))
# for i in range(1, n+1):
#     print(i)
# for i in range(2, n+1, 2):
#     print(i)
# for i in range(n, 0, -1):
#     print(i)


# 실습 2
n = int(input("N을 입력하세요: "))
total = 0
for i in range(1, n+1):
    total += i
print("합:", total)


# 실습 3
for dan in range(2, 10):     # 바깥: 2, 3단
    for su in range(1, 10):    # 안쪽: 1,2,3 (바깥 한 번마다 3번씩)
        print(f'{dan} x {su} = {dan * su}')
    print("------")
    

# 실습 4
n = int(input("측정 횟수: "))
over_count = 0
for i in range(n):
  value = int(input("측정값: "))
  if value > 80:
    over_count += 1
    
print("초과 개수: ", over_count)