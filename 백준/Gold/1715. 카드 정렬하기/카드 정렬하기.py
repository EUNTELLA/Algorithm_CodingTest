import heapq

def card_sorting(n,cards):
    heapq.heapify(cards)
    total_cost = 0
    
    while len(cards)>1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
    
        cost = a + b
        total_cost += cost
    
        heapq.heappush(cards, cost)
    return total_cost

n= int(input())
cards = [int(input()) for _ in range(n)]

print(card_sorting(n,cards))