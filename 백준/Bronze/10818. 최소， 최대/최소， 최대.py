import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

print(f"{min(nums)} {max(nums)}")
