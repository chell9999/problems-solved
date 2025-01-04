from sys import stdin

N = int(stdin.readline().strip())
times = list(map(int, stdin.readline().strip().split()))

times.sort()

times.append(times[-1])

cumul_times = []

for i in range(len(times)):
    cumul_times.append(sum(times[:i]))

print(sum(cumul_times))
