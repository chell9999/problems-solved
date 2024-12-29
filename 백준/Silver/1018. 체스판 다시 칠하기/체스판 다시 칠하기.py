import sys

N, M = map(int, sys.stdin.readline().strip().split())

board = [sys.stdin.readline().strip() for _ in range(N)]

ret = 64

for i in range(N - 7):
    for j in range(M - 7):
        cnt = [0, 0] 
        for di in range(8):
            for dj in range(8):
                if board[i + di][j + dj] == "B": # 현재 탐색하는 칸이 검은색이다
                    cnt[(di + dj) % 2] += 1 
                else: # 현재 탐색하는 칸이 흰색이다
                    cnt[(di + dj + 1) % 2] += 1
        
        ret = min(ret, min(cnt))

# 첫칸이 검은색이다
# 0번째, 2번째, 4번째... 로 짝수칸들이 검은색이여야하고 홀수칸이 흰색이여야한다

# 첫칸이 흰색이다
# 그러면 짝수칸들은 흰색이여여하고 홀수칸은 검은색이여야한다.

print(ret)
