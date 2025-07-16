
n = int(input())

eg = set()

for _ in range(n):
    eg.add(input())


sorted_eg = sorted(eg, key =  lambda x :(len(x),x))

for word in sorted_eg:
    print(word)