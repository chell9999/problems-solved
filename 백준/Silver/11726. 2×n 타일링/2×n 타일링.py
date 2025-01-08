from sys import stdin

n = int(stdin.readline().strip())
arr = [0, 1, 2]

for i in range(3, n+1):
    arr.append(arr[i-1] + arr[i-2])
    
print(arr[n] % 10007)