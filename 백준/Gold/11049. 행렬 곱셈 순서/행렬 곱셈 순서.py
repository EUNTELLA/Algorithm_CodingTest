
n= int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for term in range(1,n):
    for i in range(n-term):
        j = i + term
        
        if term == 1:
            dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
            continue
        
        dp[i][j] = float('inf')
        for k in range(i,j):
            dp[i][j] = min(dp[i][j],dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])
            
            
print(dp[0][n-1])