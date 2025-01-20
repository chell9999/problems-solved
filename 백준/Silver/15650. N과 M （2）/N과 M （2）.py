from itertools import combinations
from sys import stdin

N, M = map(int, stdin.readline().strip().split())

nums = [_ + 1 for _ in range(N)]

combs = list(combinations(nums, M))

if M == 1:
    combs.sort(key=lambda x: x[0])

    for comb in combs:
        print(f"{comb[0]}")
else:
    combs.sort(key=lambda x: (x[0], x[1]))

    for comb in combs:
        msg = " ".join(map(str, comb))
        print(msg)
