import sys

N = int(sys.stdin.readline().strip())

sort_list = []

for i in range(N):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    sort_list.append((age, name))

sort_list.sort(key=lambda x: x[0])

for age, name in sort_list:
    print(f"{age} {name}")
