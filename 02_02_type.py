# 자료형

count = 3     # int 정수
temp = 25.5   # float 실수
name = "센서A" # str 문자열

ok = True     # bool 불린형 - 참/거짓
no = False

# type() -> 자료형을 알려줌
print(type(25))       # <class 'int'>
print(type("센서A"))  # <class 'str'>
print(type(ok))       # <class 'bool'>

# 자료형마다 다른 동작
print(3 + 5)          # 8  (숫자 더하기 = 계산)
print("3" + "5")      # 35 (글자 더하기 = 이어 붙이기)
