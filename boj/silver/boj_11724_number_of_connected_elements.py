# faild: 시간 초과
import sys

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
visited = set() # <- 이거보다 리스트 인덱스 접근이 빠름

for i in range(1,n): # <- 마지막 노드 안 돌았음
    if i in visited:
        continue
    
    queue = [i]
    while queue:
        u = queue.pop(0) # <- 이게 O(n)의 시간 복잡도
        visited.add(u)

        for v in edges[u]:
            if v not in visited:
                queue.append(v)
    
    cnt += 1

print(cnt)
