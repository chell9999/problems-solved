import sys

N = int(sys.stdin.readline())

numbers = []
for i in range(N):
    number = N = int(sys.stdin.readline())
    numbers.append(number)

numbers.sort()
for i in numbers:
    print(i)
