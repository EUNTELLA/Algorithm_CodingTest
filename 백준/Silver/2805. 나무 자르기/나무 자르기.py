import sys


n, m, *rest = map(int, sys.stdin.read().split())
trees = rest  

start = 0
end = max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(tree - mid for tree in trees if tree > mid)

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
