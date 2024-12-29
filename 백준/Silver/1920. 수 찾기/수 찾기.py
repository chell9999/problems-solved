import sys

N = int(sys.stdin.readline().strip())
A_numbers = set(map(int, sys.stdin.readline().strip().split()))

M = int(sys.stdin.readline().strip())
B_numbers = list(map(int, sys.stdin.readline().strip().split()))


for number in B_numbers:
    if number in A_numbers:
        print(1)
    else:
        print(0)
