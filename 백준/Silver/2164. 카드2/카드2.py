import sys
from collections import deque

N = int(sys.stdin.readline().strip())

deck = deque()

for i in range(N):
    deck.append(i + 1)

while len(deck) > 1:
    deck.popleft()
    go_bottom = deck.popleft()
    deck.append(go_bottom)

print(deck[0])
