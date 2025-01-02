import sys

N, K = map(int, (sys.stdin.readline().strip().split()))


numbers = list(range(1, N + 1))

sequence = []
target_index = -1
while numbers:
    if target_index == -1:
        for i in range(K):
            target_index += 1
            target_index %= len(numbers)
    else:
        for i in range(K - 1):
            target_index += 1
            target_index %= len(numbers)

    target_number = numbers.pop(target_index)

    sequence.append(target_number)

print(f"<{', '.join(map(str, sequence))}>")
