import sys
input = sys.stdin.readline

m,n,l = map(int,input().split())

arr= [num for num in map(int,input().split())]
arr.sort()
total_count = 0

def binary_search(x,y):
    left =0
    right = m-1

    min_dis = float('inf')
    
    while left <= right:
        mid = (left+right)//2
        
        cur_dis = abs(arr[mid]-x)+y 
        min_dis = min(min_dis ,cur_dis)
        
        if arr[mid] <x: 
            left = mid +1
        else:
            right = mid-1
    
    return min_dis





for i in range(n):
    x,y = map(int,input().split())
    if binary_search(x,y) <=l:
        total_count +=1
print(total_count)

