# f-string - 문자열 안에 변수 바로 끼우기
# 형식: f"~~~ {변수}~~"

name = "홍길동"
age = 25
print(f'{name}님은 {age}살입니다')    # 홍길동님은 25살입니다
# 숫자도 str 변환 없이 바로 들어감
print(f'온도: {25.5}')
# 중괄호 안에 계산식 가능
hours = 3
print(f'{hours * 60}분')
# 소수점 자리수 조정
# 형식: {값(변수):.2f} -> 소수점 둘째 자리까지 (자동 반올림)
value = 25.34567
print(f'측정값: {value:.2f}')   # 측정값: 25.35
print(f'측정값: {value:.1f}')   # 측정값: 25.3


# 실습 4
raw = " 5 , sensor_2 , WARNING , 0.78912 "
parts = raw.strip().split(',')
sid = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())

print(f"[센서 {sid}] 상태 {status}, 측정값 {value:.2f}")
