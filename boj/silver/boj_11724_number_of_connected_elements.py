
import sys
from collections import deque
read = sys.stdin.readline

# n: 정점의 개수, m: 간선의 개수
n, m = map(int, read().split()) 

edges = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, read().split())
    edges[a].append(b)
    edges[b].append(a)


# search
cnt = 0  # 연결 요소의 개수
visited = [False] * (n+1)

for i in range(1,n+1): 
    if visited[i]:
        continue
    
    queue = deque([i])
    while queue:
        u = queue.popleft()
        
        for v in edges[u]:
            if not visited:
                queue.append(v)
                visited[v] = True
    cnt += 1

print(cnt)
