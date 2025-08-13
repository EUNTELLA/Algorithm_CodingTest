n = int(input())



num = list(map(int,input().split()))
count=0
v = int(input())

for i in num:
    if i == v:
        count +=1

print(count)
