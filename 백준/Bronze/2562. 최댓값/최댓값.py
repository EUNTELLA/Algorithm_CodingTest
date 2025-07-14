num = []

for _ in range(9):
    num.append(int(input()))
    
maxnum = max(num)
max_in = num.index(maxnum)+1

print(maxnum)
print(max_in)