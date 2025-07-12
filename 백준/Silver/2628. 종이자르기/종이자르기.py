x, y = map(int, input().split())  # 가로, 세로
n = int(input())  # 자르기 횟수

horizontal = [0, y] 
vertical = [0, x]

for _ in range(n):
    d, p = map(int, input().split())
    if d == 0:
        horizontal.append(p)
    else:
        vertical.append(p)

horizontal.sort()
vertical.sort()

# 최대 높이 구하기
max_h = max(horizontal[i+1] - horizontal[i] for i in range(len(horizontal)-1))
# 최대 너비 구하기
max_w = max(vertical[i+1] - vertical[i] for i in range(len(vertical)-1))

print(max_h * max_w)
