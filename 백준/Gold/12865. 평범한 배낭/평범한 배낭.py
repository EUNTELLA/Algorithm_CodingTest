mii = lambda : map(int,input().split())
N , K = mii()

W, V = [],[]

for _ in range(N):
    weight , value = mii()
    W.append(weight)
    V.append(value)
    
memo = [[0] * (K+1) for _ in range(N+1)]

for i in range(N):
    for j in range(K+1):
        pre_k = j - W[i]
        case1 = 0
        if 0 <= pre_k:
            case1 = memo[i-1][pre_k] + V[i]
        case2 = memo[i-1][j]
        memo[i][j] = max (case1, case2)
        
print(memo[i][j])