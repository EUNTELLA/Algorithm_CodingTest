import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

try:
    V, E = map(int, input().split())
    parent = [i for i in range(V + 1)]
    tree = []
    answer = 0

    for _ in range(E):
        line = input()
        if not line:
            continue
        node1, node2, grade = map(int, line.strip().split())
        tree.append([grade, node1, node2])

    tree.sort()

    for grade, node1, node2 in tree:
        if find(node1) != find(node2):
            union(node1, node2)
            answer += grade

    print(answer)

except Exception as e:
    print("Error:", e, file=sys.stderr)
