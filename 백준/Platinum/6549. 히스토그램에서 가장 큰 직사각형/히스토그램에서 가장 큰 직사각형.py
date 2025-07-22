import sys
input = sys.stdin.readline
while True:
    arr = list(map(int, input().split()))
    n = arr[0]          # 맨 앞의 숫자: 막대(직사각형) 개수
    if n == 0:          # -> 막대(직사각형) 개수 0이면 반복문 종료(프로그램 끝)
        break
    # 높이만 따로 리스트로 저장(맨 끝에 0 추가: 스택에 남은 값까지 모두 처리하기 위함)
    height = arr[1:] + [0]
    stack = []              # 스택(바구니): 인덱스를 저장
    max_height = 0          # 지금까지 찾은 가장 넓은 직사각형 넓이 저장
     # 0번부터 마지막(추가된 0까지) 모든 막대 순회
    for i in range(len(height)):
        while stack and height[stack[-1]] > height[i]:      # 지금 막대 높이보다 더 높은 막대가 스택에 남아있으면 꺼내면서 넓이 계산
            h= height[stack.pop()]                          # pop된 인덱스의 높이
            # pop된 막대의 확장 가능한 가로 길이 계산
            if not stack:
                w = i                       # 왼쪽에 '나보다 작은' 벽이 없다면 0번부터 i-1까지 모두 확장
            else:
                w = i - stack[-1] -1        # '나보다 낮은' 블록 다음 칸부터 i-1까지 확장
            max_height = max(max_height, h*w)         # 넓이(h * w)와 지금까지의 최대 넓이(max_h) 중 큰 값을 저장
        stack.append(i)                     # 현재 막대의 인덱스를 스택에 쌓음
    print(max_height)                            # 한 케이스(입력 한 줄)가 끝나면 결과(최대 넓이)를 출력
