import sys
while True:
    sides = list(map(int, sys.stdin.readline().strip().split()))
    sides = sorted(sides)
    
    if 0 in sides:
        break
    
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print("right")
    else:
        print("wrong")