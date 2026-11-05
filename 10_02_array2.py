import numpy as np

# 인덱싱, 슬라이싱
# a = np.array([0,1,2,3,4])
# print(a[0], a[-1])       # 0 4 
# print(a[1:4])     # [1 2 3]
# print(a[::2])     # [0 2 4]

# # 배열 연산
# a = np.array([1,2,3])
# b = np.array([10,20,30])
# print(a + b)     # [11, 22, 33]
# # 같은 위치 값끼리 계산 (반복문 필요X)
# # 사칙연산 모두 같은 방식으로 계산

# # 스칼라 연산
# # - 숫자 하나를 배열 전체에 적용, 크기를 맞출 필요가 없다
# # - 연산 숫자는 수학과 같아 곱하기 먼저
# print(a * 10 + 3)

# # 브로드캐스팅
# table = np.array([[72, 2.4], [95, 6.8]])
# print(table.shape)  # (2,2)
# base = np.array([70, 2.0])   # (,2)
# print(table - base)
# #[[ 2.   0.4]
# # [25.   4.8]]
# # 한 줄짜리 기준값이 모든 행에 퍼져서 계산됨
# # 조건) 작은 쪽 크기가 1이거나 같아야 함


# # 비교 연산과 불리언 배열
# vals = np.array([70, 95, 71, 88, 73])
# print(vals > 75)      # [False  True False  True False]

# # 불리언 인덱싱
# # - 조건이 참/거짓인 배열을 만듦 -> 그 배열을 대괄호에 넣으면 참인 값만 남는다
# print(vals[vals > 75])    # [95 88]

# # np.where(조건, 참일 때 값, 거짓일 때 값)
# print(np.where(vals > 85, 1, 0))    # [0 1 0 1 0]

# # 다중 조건
# print(vals[(vals > 70) & (vals < 90)])   # [71 88 73]



# # 통계 
# # - 정상을 알아야 이상을 알 수 있다
# # ex) 평균을 알아야 평균과 크게 차이가 나는 값이 나왔을 때 이상치 판단 가능
# # - 평균, 최대/최소, 표준편차, 분산
# # - NumPy 에서 함수 하나로 계산

# s = np.array([70, 72, 71, 95, 73])
# print("합계:", s.sum())
# print("평균:", s.mean())
# print("중앙값:", np.median(s))
# print("최대:", s.max())
# print("최소:", s.min())

# # 분산
# stable = np.array([70, 71, 70, 72, 71])
# unstable = np.array([60, 85, 65, 95, 70])
# print(round(stable.var(), 1))     # 0.6
# print(round(unstable.var(), 1))   # 170.0

# # 표준편차
# print(round(stable.std(), 2))
# print(round(unstable.std(), 2)) # 13.04

# # axis 개념 (행/열 방향)
# mat = np.array([[70, 2.1], [72, 2.3]])
# print(mat.mean(axis=0))     # 열별 평균 (센서별)
# print(mat.mean(axis=1))     # 행별 평균 (시점별)  -> 지금은 큰 의미X
# print(mat.mean())           # 전체 평균


# 파일에서 배열로 불러오기(np.loadtxt)

rpm = np.loadtxt('data/10_mct_tool.csv',
                 delimiter=",",      # 값을 나누는 기호
                 skiprows=1,        # 첫 줄(제목)은 건너뜀
                 usecols=4)         # 5번째 열 = 회전수
# print(rpm)

rpm_tq = np.loadtxt('data/10_mct_tool.csv',
                 delimiter=",",      # 값을 나누는 기호
                 skiprows=1,        # 첫 줄(제목)은 건너뜀
                 usecols=(4,5))  
print(rpm_tq.shape)       # (40, 2)