def is_enough(height):
    return sum (tree - height for tree in trees if tree > height) >= m

n,m = map(int,input().split())

trees = list(map(int, input().split()))

low = 0 
high = max(trees)
answer =0

while low <= high:
    mid = (low + high) // 2

    if is_enough(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)