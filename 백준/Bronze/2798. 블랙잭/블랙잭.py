import sys
from itertools import combinations

N, M = list(map(int, sys.stdin.readline().strip().split()))
cards = list(map(int, sys.stdin.readline().strip().split()))

all_combinations = list(combinations(cards, 3))

sums = []

for combination in all_combinations:
    sums.append(sum(combination))

sums = sorted(sums, reverse=True)

for sum in sums:
    if sum <= M:
        print(sum)
        break
