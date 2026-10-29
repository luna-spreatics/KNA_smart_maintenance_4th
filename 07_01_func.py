# 함수
# 함수의 기본 구조
# 형식:
# def 함수이름():
#   실행할 코드

def greet():
    print("점검을 시작합니다")


# 정의만으로는 실행 안됨 -> 호출해야 실행
# 호출: 함수 이름 적고 괄호를 붙이기
# greet()


# 실습 3
# hello()           # NameError (정의 전 호출 시)
def hello():
    print("안녕하세요")
    
hello()
hello()


# 실습 4
def line():
    print("=" * 10)

def check():
    print("점검을 시작합니다")
    print("기록을 준비하세요")
    
line()
check()

line()
check()