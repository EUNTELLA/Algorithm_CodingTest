n = int(input())

pos = []
for _ in range(n):
    x,y = map(int,input().split())
    pos.append((x,y))
    
pos.sort()

def solve(left,right):
    if left == right:
        return 10**9
    if right - left == 1:
        return (pos[right][0]- pos[left][0])**2 +(pos[right][1]- pos[left][1])**2
    
    mid = (left + right)//2
    
    left_min = solve(left,mid)
    right_min = solve(mid , right)
    temp = min(left_min,right_min)
    
    mid_min = calculate_mid(temp,mid, left,right)
    
    return mid_min

def calculate_mid(temp,mid,start,end):
    nears=[]
    for i in range(start, end+1):
        if (pos[mid][0]- pos[i][0])**2 <=temp:
            nears.append(pos[i])
            
    nears.sort(key=lambda x : x[1])
            
    min_distance = temp
    
    for i in range(0,len(nears)):
        nears_1 = nears[i]
        for j in range(i+1,len(nears)):
            nears_2 = nears[j]
            
            if min_distance <= (nears_1[1]-nears_2[1])**2:
                break
            
            nears_dis = (nears_2[0]-nears_1[0])**2 + (nears_2[1]-nears_1[1])**2
            min_distance =min(min_distance,nears_dis)
            
            
    return min_distance

print(solve(0,n-1))