import sys 
input = sys.stdin.readline

n = int(input())

n_array = list(map(int,input().split()))
 
m = int(input())

m_array =list(map(int,input().split()))

n_array.sort()

def binary_search (target):
    start = 0
    end = n-1
    
    while start <= end:
        mid = (start + end) //2
        
        if n_array[mid] == target:
            return 1

        if n_array[mid]<target:
            start = mid + 1
            
        else:
            end = mid - 1
    return 0

for q in m_array:
    print(binary_search(q),end=" ")


