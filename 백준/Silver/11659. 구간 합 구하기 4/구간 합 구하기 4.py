from sys import stdin

N, M = map(int, stdin.readline().strip().split())
numbers = list(map(int, stdin.readline().strip().split()))

cumul_sums = [0]

sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
    cumul_sums.append(sum)


for i in range(M):
    i, j = map(int, stdin.readline().strip().split())
    print(cumul_sums[j] - cumul_sums[i - 1])
