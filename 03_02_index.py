# 인덱싱 - 위치 번호로 글자 하나 꺼내기
# 형식: 문자열[번호]   (첫 글자 = 0번)

word = 'PYTHON'
# word = 'SIGNAL'
print(word[0], word[2], word[5])      # P T N
# 음수 인덱스: 뒤에서부터 -1, -2,...
print(word[-1], word[-2])             # N O

# print(word[6])        # IndexError: string index out of range


# 슬라이싱 - 구간으로 잘라내기
# 형식: 문자열[시작:끝] (시작 포함, 끝 제외)
print(word[1:4])    # YTH
# 생략 가능
# - 시작 생략 = 처음부터 (0번부터)
# - 끝 생략 = 끝까지
# - 둘다 생략 = 전체
print(word[:3])       # PYT
print(word[3:])       # HON
print(word[:])        # PYTHON
# 음수
print(word[-3:])      # HON
print(word[:-1])      # PYTHO

# step 간격 주기
# 형식: 문자열[시작:끝:간격]
print(word[::2])      # PTO
print(word[1::3])     # YO
