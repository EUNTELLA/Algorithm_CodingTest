a , b = map(int,input().split())

c = int(input())

totalmin = a *60 + b + c

hour = (totalmin //60) % 24
minute = totalmin % 60
    
print(hour, minute)
    