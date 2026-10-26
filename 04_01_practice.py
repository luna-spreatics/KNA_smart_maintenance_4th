# 실습 2
temps = [22, 24, 27, 29, 26, 23]
print(temps[0], temps[2], temps[-1])

# 실습 3
output = [120, 95, 130, 110, 88, 102]
first = output[0]
last = output[-1]
print(first + last)
print((first + last) / 2)

# 실습 4
temps = [22, 24, 27, 29, 26, 23, 25, 28, 30, 21]
print(temps[:3])
print(temps[-3:])
print(len(temps[:3]))

# 실습 5
hours = [3, 4, 5, 6, 5, 4, 6, 7, 8, 7, 5, 3]
first = hours[:6]
second = hours[6:]
print(first)
print(second)
print(len(first), len(second))

# 실습 6
temps = [25, 26, 240, 28, 27]
print(240 in temps)
i = temps.index(240)
temps[i] = 24
print(temps)
print(240 in temps)

# 실습 7
temps = []
temps.append(30)
print(temps)
temps.insert(0, 28)
print(temps)
temps.extend([31, 32])
print(temps)

# 실습 8
temps = [25, 26, 999, 24, 28, 26]
temps.remove(999)
print(temps)
x = temps.pop(1)
print(x)
del temps[0]
print(temps)

# 실습 9
temps = [27, 24, 30, 22, 26, 24, 28]
temps.sort()
print(temps)
temps.reverse()
print(temps)
print(temps.count(24))
print(temps.index(24))
