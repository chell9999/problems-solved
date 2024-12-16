import sys

nums = [int(x) for x in sys.stdin.readline().split()]

s = ""
for i in range(7):
    if nums[i + 1] - nums[i] > 0:
        s += "a"
    else:
        s += "d"

if "d" not in s:
    print("ascending")
elif "a" not in s:
    print("descending")
else:
    print("mixed")
