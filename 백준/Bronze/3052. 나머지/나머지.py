arr = []

for _ in range(10):
    n = int(input()) 
    
    t = n%42
    arr.append(t)    
re=set(arr)
print (len(re))
    
    
    