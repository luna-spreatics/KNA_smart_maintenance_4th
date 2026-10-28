# 셋 - 중복 자동 제거, 순서 없음
# 형식: {값1, 값2} 또는 set(리스트)
# - 빈 셋 set()
logs = ["S01", "S02", "S01", "S03"]
unique_logs = set(logs)
print(unique_logs)  # {'S02', 'S01', 'S03'} / 셋은 순서가 없어 인덱싱 불가
print(sorted(unique_logs))      # ['S01', 'S02', 'S03']

# add - 값 추가 / in - 포함 확인
alerts = {"S01", "S02"}
alerts.add("S03")
print(alerts)
alerts.add("S02")
print(alerts)
print("S02" in alerts)


# 집합 연산 - union(전체) / intersection(공통) / difference(차이)
line_a = {"S01", "S02", "S03"}
line_b = {"S03", "S04"}
print(line_a.union(line_b))
print(line_a.intersection(line_b))
print(line_a.difference(line_b))