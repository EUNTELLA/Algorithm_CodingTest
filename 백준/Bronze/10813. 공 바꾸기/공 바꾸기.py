n,m = map(int,input().split())
ball = list(range(1,n+1))

for _ in range(m):
    i,j = map(int,input().split())   

    temp = ball[i-1]
    ball[i-1] = ball[j-1]
    ball[j-1] = temp
    
    
print(*ball)

            