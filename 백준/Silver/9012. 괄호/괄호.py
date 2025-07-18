


def check_e (e):
    stack = []
    for char in e:
        if char =='(':
            stack.append(char)
        elif char==")":
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

n = int(input())
for _ in range(n):
    ex = input().strip()
    print(check_e(ex))