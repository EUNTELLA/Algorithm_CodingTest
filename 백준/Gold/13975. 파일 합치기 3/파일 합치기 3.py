import heapq
import sys

def file_sorting(all_cards):
    heapq.heapify(all_cards)
    file_size = 0
    
    while len(all_cards) >1 :
        a = heapq.heappop(all_cards)
        b = heapq.heappop(all_cards)
        
        size = a + b
        file_size += size
        
        heapq.heappush(all_cards,size) 
    return file_size

n = int(input())

for _ in range(n):
    k = int(input())
    cards = list(map(int,input().split()))
    print(file_sorting(cards))