import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
numbers_to_count = list(map(int, sys.stdin.readline().strip().split()))

counts = {}
for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

output = []

for number in numbers_to_count:
    if number in counts.keys():
        output.append(counts[number])
    else:
        output.append(0)


print(" ".join(map(lambda x: str(x), output)))
