import numpy as np

# 리스트 vs 배열
# 1) 리스트
# - 서로 다른 자료형도 같이 존재 가능
# - 계산이 느리고 반복문을 돌아야 한다
list = [70, 72, 71]
print(list *2)      # [70, 72, 71, 70, 72, 71]
print([v * 2 for v in list])      # [140, 144, 142]

# 2) 배열
# - 같은 자료형만 존재 가능
# - 계산이 빠르다

temp = np.array([70, 72, 71])
print(temp)       # [70 72 71]

print(temp + 2)   # [72 74 73] ->  반복문 없는 묶음 계산

# 튜플로 배열 만들기
print(np.array((1, 2, 3)))      # [1 2 3]

# 배열 생성
# np.arange(시작, 끝, 간격) : 연속 정수
# - 끝값은 포함되지 않음
print(np.arange(5))     # [0 1 2 3 4]
print(np.arange(0, 10, 2))      # [0 2 4 6 8]

# np.linspace(시작, 끝, 개수) : 균등 분할
# - 끝값 포함
print(np.linspace(0, 1, 5))   # [0.   0.25 0.5  0.75 1.  ]
print(np.linspace(0, 10, 5))   # [ 0.   2.5  5.   7.5 10. ]


# 배열 속성
# - ndim, shape, size, dtype
# - 속성은 괄호X

a = np.array([1,2,3])
b = np.array([[1,2,3], [4,5,6]])

print("dim:",a.ndim, b.ndim)     # dim: 1 2
print("shape:", a.shape, b.shape)   # shape: (3,) (2, 3)
print("size:", a.size, b.size)    # size: 3 6


# reshape() 로 형태 바꾸기
# - -1 사용 시 자동 계산 (행 또는 열에 한번만 사용)
c = np.arange(12)
print(c.reshape(3, 4))
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# flatten() -> 1차원 만듦
b3 = np.array([[1, 2, 3], [4, 5, 6]])
print(b3.flatten())   # [1 2 3 4 5 6]