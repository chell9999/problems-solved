import sys

A, B = list(map(int, sys.stdin.readline().split()))


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


print(gcd(A, B))
print(lcm(A, B))
