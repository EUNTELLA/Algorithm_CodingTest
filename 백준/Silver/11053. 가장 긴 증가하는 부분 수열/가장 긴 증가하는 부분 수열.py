import sys
input = sys.stdin.readline

n = int(input())

arr= list(map(int,input().split()))

result = []

def binary_search(target):
    
    left = 0
    right = len(result) -1
    
    while left <= right:
        mid = (left + right)//2
        
        if result[mid] == target:
            return mid
        elif result[mid] <target:
            left = mid + 1
            
        else:
            right = mid-1
    
    
    return left #가장 최근의 mid값이 left 로 이동


for number in arr :
    if len(result) ==0:
        result.append(number)
        continue

    max_val = result[-1]



    if number > max_val:
        result.append(number)
    else: #number < max_val
        index = binary_search(number)
    
        result [index] = number

print(len(result))
    
    

    
    
