import sys

N = int(sys.stdin.readline())

for i in range(9):
    multiplication = i + 1
    result = N * multiplication
    print(f"{N} * {multiplication} = {result}")