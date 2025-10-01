import sys
from collections import deque

read = sys.stdin.readline

n, m = map(int, read().split())
maze = [[0 for _ in range(m+2)] for _ in range(n+2)] # 가장자리에 padding

for i in range(1,n+1):
    input = read()
    for j in range(1, m+1):
        maze[i][j] = int(input[j-1])

cost = [[n*m+1 for _ in range(m+2)] for _ in range(n+2)]

# 방향: 왼, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

queue = deque([(1,1)])
cost[1][1] = 1

while queue:
    px, py = queue.popleft()

    for i in range(4):
        x, y = px+dx[i], py+dy[i]

        # 값이 1(갈 수 있는 길)이고 더 빠른 길이면
        if maze[x][y] and cost[x][y] > cost[px][py] + 1:
                queue.append((x, y))
                cost[x][y] = cost[px][py] + 1

print(cost[n][m])
