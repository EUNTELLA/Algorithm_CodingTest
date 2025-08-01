import sys
input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

min_cost = 10 ** 9
visited = [False]*n

def solve(start_city, current_city,cost, city_count):
    global min_cost
    
    if cost > min_cost: 
        return
    
    if city_count == n:
        if w[current_city][start_city] == 0:
            return
        cost += w[current_city][start_city]
        min_cost = min(min_cost,cost)
        return

    for next_city in range(n):
        if not visited[next_city] and w[current_city][next_city] != 0:
            visited[next_city] = True
            solve(start_city,next_city, cost +
                  w[current_city][next_city],city_count+1)
            visited[next_city] = False

for start_city in range(n):
    visited[start_city]= True
    solve(start_city,0,0,1)
sys.stdout.write(str(min_cost))