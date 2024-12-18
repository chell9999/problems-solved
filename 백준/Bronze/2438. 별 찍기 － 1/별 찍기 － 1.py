import sys

N = int(sys.stdin.readline())

count = 0
for i in range(N):
    count += 1
    print("*" * count)
