# 실습 1
a = 17
b = 5
print(a + b)    # 22
print(a - b)    # 12
print(a * b)    # 85
print(a / b)    # 3.4   (나눗셈은 실수)
print(a // b)   # 3     (몫)
print(a % b)    # 2     (나머지)
print(a ** b)   # 1419857  (거듭제곱)

# 실습 2
x = 80
y = 91
z = 90
print((x + y + z) / 3)   # 87.0  (평균)
side = 7
print(side ** 2)         # 49    (정사각형 넓이)
print(3 * 4 * 5)         # 60    (직육면체 부피)

# 실습 3
print(5 == 5)   # True
print(5 != 3)   # True
print(7 > 10)   # False
print(7 < 10)   # True
print(5 >= 5)   # True
print(4 <= 3)   # False

# 실습 4
temp = 85
temp_ok = 60 <= temp and temp <= 90
print(temp_ok)                # True
pressure = 5
pres_ok = 3 <= pressure and pressure <= 7
print(pres_ok)                # True
print(temp_ok and pres_ok)    # True  (둘 다 정상)

# 실습 5
stock = 100
stock += 50
print(stock)   # 150  (입고)
stock -= 30
print(stock)   # 120  (출고)
stock += 5
print(stock)   # 125  (반품)

# 실습 6
total = 500
defect = 23
print(defect / total * 100, "%")   # 4.6   (불량률 %)
run_h = 21
all_h = 24
print(run_h / all_h * 100, "%")    # 87.5  (가동률 %)

# 실습 7
minutes = 500
print(minutes // 60)   # 8   (시간)
print(minutes % 60)    # 20  (분)
print(minutes // 60, "시간", minutes % 60, "분")
