T = int(input())
 
for _ in range(T):
    R,S = input().split()
    R=int(R)
    
    for C in S:
        print(C*R,end='')
        
    print()