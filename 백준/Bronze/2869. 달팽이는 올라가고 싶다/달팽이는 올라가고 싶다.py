
A,B,V = map(int,input().split())



N = (V-B)/(A-B)

if N == int(N):
    print(int(N))
else:
    print(int(N)+1)