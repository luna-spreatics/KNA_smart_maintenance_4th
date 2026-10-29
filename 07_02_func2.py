# 매개변수와 반환값

# 매개변수와 인자
# 형식:
# def 함수이름(매개변수):
#   ....
# 호출
# 함수이름(인자)

def check(name):        # name = 매개변수
    print(name + " 점검을 시작합니다.")


check("압축기1")        # "압축기1" = 인자
check("펌프1")
# check()    # TypeError: check() missing 1 required positional argument: 'name'
# check("A", "B")   # TypeError: check() takes 1 positional argument but 2 were given


# 키워드 인자
def report(name, temp):
  print(name, temp, "도")
  
report(temp=78, name="펌프")

# return
# - print: 사람이 확인할 수 있게 출력 / return : 값을 프로그램에게 돌려줘서 이어 쓸 수 있게 한다
def add(a, b):
  return a+b
  print("실행 안됨")        # return을 만나면 즉시 함수 종료 -> 그 아래 코드는 실행 X

total = add(3, 4)
print(total)

# 여러 값 반환 / 언패킹
# - 쉼표로 여러 값을 return 하면 튜플로 묶여서 돌아옴 -> 언패킹 가능
def min_max(values):
  return min(values), max(values)

print(min_max([75, 10, 100]))   # (10, 100)
low, high = min_max([75, 10, 100])
print(low, high)

none = report("펌프", 10)
print(none)     # None -> return 값이 없는 함수 호출해서 변수로 받을 경우 None