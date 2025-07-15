import sys
n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))
    
nums.sort()

for num in nums:
    sys.stdout.write(str(num) + '\n')