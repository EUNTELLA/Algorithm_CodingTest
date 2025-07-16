from itertools import combinations

nank = [int(input()) for _ in range(9)]  # 괄호 수정

for comb in combinations(nank, 7):
    if sum(comb) == 100:
        for height in sorted(comb):
            print(height)
        break  # 여기서 루프 종료
