# failed: 틀림

# 1. 두 수 중 작은 수를 키값으로 하는 딕셔너리를 만든다.
# 2. 딕셔너리에서 노드1과 연결된 노드들을 큐에 넣는다.
# 3. 큐에서 뺀, 다음 방문할 노드와 연결된 노드들을 딕셔너리에서 찾아 큐에 넣는다.
# 4. 방문한 노드는 중복이 없는 set 타입의 visited로 표시
# 5. 큐가 빌 때까지 반복

import sys

read = sys.stdin.readline

n = int(read())
pn = int(read())

pairs = {}
for _ in range(pn):
    a, b = map(int, read().split())
    if min(a,b) not in pairs:
        pairs[min(a, b)] = []
    
    pairs[min(a,b)].append(max(a,b)) #<- 양쪽 다 적어줘야 함


queue = [1]
visited = set()
while queue:
    cur = queue.pop(0)
    visited.add(cur)

    for node in pairs.get(cur, []):
        if node not in visited:
            queue.append(node)

print(len(visited)-1)
print(visited)
