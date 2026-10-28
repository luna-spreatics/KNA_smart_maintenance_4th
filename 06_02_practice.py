# 실습 1
sensors = {"모터온도": 78, "진동": 0.5}
print(sensors["모터온도"])     # 78
sensors["압력"] = 95           # 추가
sensors["모터온도"] = 80       # 수정
print(sensors)
print(sensors.get("유량", 0))  # 0 (없으면 기본값)
print("진동" in sensors)       # True


# 실습 2
sensors = {"모터온도": 78, "진동": 0.5}
new_data = {"모터온도": 81, "압력": 95}
sensors.update(new_data)
print(sensors)
del sensors["진동"]
print("센서 수:", len(sensors))   # 센서 수: 2


# 실습 3
sensors = {"온도": 80, "진동": 55, "압력": 95}
avg = sum(sensors.values()) / len(sensors)
print("평균:", round(avg, 1))

top = ""
high = 0
for name, value in sensors.items():
    if value > high:
        high = value
        top = name

print("최댓값 센서:", top, high)

# 실습 4
names = ["온도", "진동", "압력"]
values = [78, 0.5, 95]
sensors = dict(zip(names, values))
print(sensors) 
for name, value in sensors.items():
  print(name, value)
  

# 실습 5
values = {"온도": 95, "진동": 0.5, "압력": 88}
limits = {"온도": 90, "진동": 1.0, "압력": 90}
warning = []
for name, value in values.items():
    if value > limits[name]:
        warning.append(name)
print("경고 센서:", warning)   # ['온도']

# 실습 6
plant = {
  "1번모터": {"온도": 78, "상태": "정상"},
  "2번펌프": {"압력": 95, "상태": "경고"}
}

print(plant["2번펌프"]["압력"])

for name, info in plant.items():
  if info["상태"] == "경고":
    print(name, "점검 필요")
    

# 실습 7
rows = ["온도,78", "압력,95", "진동,0.5"]
sensors = {}
for row in rows:
  name, value = row.split(",")
  sensors[name] = float(value)
print(sensors)

# 실습 8
sensors = {"온도": 95, "압력": 96}
limits = {"온도": 90, "압력": 90}

# values() 이용한 평균
avg = sum(sensors.values()) / len(sensors)
print("평균:", round(avg, 1))

# items() 순회 -> 임계값 비교 -> 초과한 값은 셋에 담기(키 값 담기)
danger = set()
for name, v in sensors.items():
  if v > limits[name]:
    danger.add(name)

# 셋 정렬하여 출력
print("위험 센서:", sorted(danger))