#회의실 
#끝나는 시간이 빠른 순으로 정렬
# 빨리 끝나면 그 뒤에 더 많은 회의를 배정할 수 있음


n = int(input())
arr= []

for _ in range(n):

    
    start, end = map(int, input().split())
    arr.append((start, end))
    
arr.sort(key= lambda x: (x[1], x[0])) #끝나는 시간 오름차순, 같을 경우 시작시간 오름차순
    
count = 0
end_time = 0

for start, end in arr:
    if start >= end_time:  # 시작 시간이 이전 회의의 끝나는 시간보다 크거나 같으면
        count += 1
        end_time = end  # 현재 회의의 끝나는 시간을 갱신    

print(count)