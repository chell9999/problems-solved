import sys

N = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))

prime_numbers = []
for number in numbers:
    no_remainder_numbers = []
    for i in range(1, number + 1):
        if number % i == 0:
            no_remainder_numbers.append(i)
    if no_remainder_numbers == [1, number]:
        prime_numbers.append(number)

print(len(prime_numbers))
