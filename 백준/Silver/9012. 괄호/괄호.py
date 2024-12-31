import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    sequence = sys.stdin.readline().strip()

    stack = []

    for i in sequence:
        stack.append(i)
        if len(stack) >= 2:
            if stack[-2] == "(" and stack[-1] == ")":
                stack.pop()
                stack.pop()

    if stack:
        print("NO")
    else:
        print("YES")
