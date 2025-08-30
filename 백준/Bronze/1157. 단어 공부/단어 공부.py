s = input()

count = 0
al = s.upper()
a = set(al)

result = ''

for c in a:
    if al.count(c) > count:
        count = al.count(c)
        result = c
    elif al.count(c) == count :
        result = "?" 
        
print(result)
    
    