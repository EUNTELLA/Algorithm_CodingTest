n,m = map(int,input().split())
ball = list(range(1,n+1))

for _ in range(m):
    i,j = map(int,input().split())   

    temp = ball[i-1:j]
    temp.reverse()
    ball[i-1:j] = temp
  
for i in range(n):
    print(ball[i],end=" ")