# 실습 2
def report(name, temp):
  print(name, temp, "도")
  
report("모터", 78)
report("펌프", 92)

# 실습 4
def cal_avg(a, b):
  return (a + b) / 2

avg = cal_avg(80, 90)
print(avg)
print(avg * 2)


# 실습 5
def stats(v):
  return min(v), max(v), sum(v) / len(v)

lo, hi, avg = stats([78, 92, 85])

print(lo, hi, avg)