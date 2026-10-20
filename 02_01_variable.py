# 변수와 할당 - 값에 이름 붙이기
# 형식: 변수이름 = 값 <- 오른쪽 값을 왼쪽 이름에 "저장"하라는 명령
temp = 25
name = "센서A"
count = 3

print(temp)  # 25
print("temp")
x = 10
x = x + 5
print(x)  # 15

# 변수 이름 규칙
# 형식: 영문자,숫자,밑줄 사용 가능 / 숫자로 시작 불가 / 공백 불가
sensor_count = 3      # snake_case
temp2 = 10            # 숫자 사용 가능 (숫자로 시작X)
# 2temp = 2           # SyntaxError: invalid decimal literal

# 대소문자 구분, 재할당
temp = 25
Temp = 100
print(temp, Temp)   # 25 100
# 재할당: 마지막에 저장한 값만 남음
score = 10
score = 20
score = 30
print(score)        # 30


print("---------------------------")
# 실습1
print("실습1")
temp = 25
print(temp)
name = "센서A"
print(name)

print("실습2")
temp = 30
print(temp)
temperature = temp
print(temperature)

print("실습3")
my_number = 7
print(my_number)
mood = "행복"
print(mood)

print("실습4")
age = 27
label = "나이"
print(label)
print(age)
