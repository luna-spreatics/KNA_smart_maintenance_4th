# 입력 (input)
# 주의) 사용자 입력은 항상 "문자열"
# 형식: 변수 = input("안내문구: ")
# name = input("이름: ")
# age = input("나이: ")
# print(name)

# 형변환 - int(), float(), str()
# print(age + 1)      # TypeError
# print(int(age) + 1)   # int() 형변환 후 연산
height = float("173.5")   # float() 실수 변환
print(height, type(height))

print("나이:" + str(30))