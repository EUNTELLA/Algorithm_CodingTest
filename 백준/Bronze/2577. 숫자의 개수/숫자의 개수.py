# 입력을 세 줄로 받기
A = int(input())
B = int(input())
C = int(input())

# 곱셈 결과
product = A * B * C

# 0부터 9까지 카운트를 위한 리스트
counts = [0] * 10

# 문자열로 바꿔서 각 자리수 세기
for ch in str(product):
    counts[int(ch)] += 1

# 결과 출력: 0부터 9까지
for cnt in counts:
    print(cnt)
