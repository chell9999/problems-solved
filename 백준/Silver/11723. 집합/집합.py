from sys import stdin

N = int(stdin.readline().strip())

the_set = set()

for _ in range(N):
    input = stdin.readline().strip().split()
    command = input[0]
    if len(input) >= 2:
        element = int(input[1])

    if command == "add":
        if element not in the_set:
            the_set.add(element)
    elif command == "remove":
        if element in the_set:
            the_set.remove(element)
    elif command == "check":
        if element in the_set:
            print(1)
        else:
            print(0)

    elif command == "toggle":
        if element in the_set:
            the_set.remove(element)
        else:
            the_set.add(element)
    elif command == "all":
        the_set = set([_ + 1 for _ in range(20)])
    elif command == "empty":
        the_set = set()
