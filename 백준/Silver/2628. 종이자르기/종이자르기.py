x, y = map(int, input().split())  # 종이의 가로(x), 세로(y)
n = int(input())  # 자르는 횟수 입력

horizontal = [0, y]  # 가로 자르기를 위한 리스트 (세로 기준), 위(0)와 아래끝(y) 포함
vertical = [0, x]    # 세로 자르기를 위한 리스트 (가로 기준), 왼쪽(0)과 오른쪽끝(x) 포함

for _ in range(n):
    d, p = map(int, input().split())  # d는 방향(0: 가로, 1: 세로), p는 자르는 위치
    if d == 0:
        horizontal.append(p)  # 가로 자르기 → 세로 위치에 절단선 추가
    else:
        vertical.append(p)    # 세로 자르기 → 가로 위치에 절단선 추가

horizontal.sort()  # 절단선 오름차순 정렬 (인접 간격 계산을 위해)
vertical.sort()

# 인접한 절단선 사이의 최대 간격 = 가장 큰 조각의 높이
max_h = max(horizontal[i+1] - horizontal[i] for i in range(len(horizontal)-1))

# 인접한 절단선 사이의 최대 간격 = 가장 큰 조각의 너비
max_w = max(vertical[i+1] - vertical[i] for i in range(len(vertical)-1))

print(max_h * max_w)  # 가장 큰 조각의 넓이 출력
