import sys
input = sys.stdin.readline
n = int(input())

n_array = set(map(int,input().split()))

m = int(input())
m_array = list(map(int,input().split()))

for num in m_array:
    print(1 if num in n_array else 0)

# n_array.sort()
# for m in m_array:
#     if m in n_array:
#         print(1)
#     else: 
#         print(0)
        
# def binart_search(k):
#     start = 0
#     end = n-1
#     while start <= end:
#         mid = (start + end) //2
#         if n_array[mid] == k:
#             return 1
#         if n_array[mid]< k:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 0

# for q in m_array:
#     print(binart_search(q))