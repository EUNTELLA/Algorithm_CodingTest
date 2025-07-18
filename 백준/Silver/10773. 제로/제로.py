k = int(input())
data = []

for _ in range(k):
    d = int(input())
    if d == 0:
        if data:
            data.pop()
    else:
        data.append(d)

print(sum(data))
