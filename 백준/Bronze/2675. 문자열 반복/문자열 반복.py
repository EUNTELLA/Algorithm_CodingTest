s = int(input())

for _ in range(s):
    r , p = input().split()
    r = int(r)
    
    for c in p:
        print(c*r,end="")

    print()