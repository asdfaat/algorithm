

# 1. 방향이 없는 그래프 특성에 맞게 연결 정보를 담은 리스트를 생성한다.
# 2. 리스트에서 노드1과 연결된 노드들을 큐에 넣는다.
# 3. 큐에서 뺀, 다음 방문할 노드와 연결된 노드들을 큐에 넣는다.
# 4. 방문한 노드는 중복이 없는 set 타입의 visited로 표시
# 5. 큐가 빌 때까지 반복

import sys
from collections import deque
read = sys.stdin.readline

n = int(read())
pn = int(read())

edges = [[] for _ in range(n+1)]
for _ in range(pn):
    a, b = map(int, read().split())
    edges[a].append(b)
    edges[b].append(a)



queue = deque([1])
visited = set()
while queue:
    cur = queue.popleft()

    
    for node in edges[cur]:
        if node not in visited:
            queue.append(node)
            visited.add(node)
num = max(0, len(visited)-1)
print(num) 
