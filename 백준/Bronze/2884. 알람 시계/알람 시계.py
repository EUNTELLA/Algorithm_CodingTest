h, m = map(int, input().split())

s = m - 45
if s < 0:
    h = (h - 1) % 24
    m = s + 60
else:
    m = s

print(h, m)
