n , k = map(int,input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))
   
count = 0   

for i in range(n-1,-1,-1):
    #역순으로 가장 큰 동전부터 확인 (마지막인덱스, 0번까지, 1씩 감소)
    if k>= coins[i]:
        #현재 남은 금액(k) >= 현재 동전 가치
        count += k//coins[i]
        #현재 동전으로 만들 수 있는 최대 개수
        k %= coins[i]
        #현재 동전 사용 후 남은 금액 (나머지)
        # k =4200, coins[i] = 1000일때 -> 4200 % 1000 = 200
        
    if k == 0:
        #남은 금액이 0이면 종료
        break
print(count)