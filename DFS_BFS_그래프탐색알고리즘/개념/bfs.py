#bfs

from collections import deque as d

# 각 노드가 연결된 정보를 표현
graph = [
    [], # 0번 노드, 보통 1번 노드부터 시작해서 빈칸으로 만듬
    [2, 3, 8], # 1번 노드 2, 3, 8 연결
    [1, 7], # 2번 노드 1, 7 연결
    [1, 4, 5], # 3번 노드 1, 4, 5 연결
    [3, 5], # 4번 노드 3, 5 연결
    [3, 4], # 5번 노드 3, 4 연결
    [7], # 6번 노드 7 연결
    [2, 6, 8], # 7번 노드 2, 6, 8 연결
    [1, 7] # 8번 노드 1, 7 연결
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    q = d([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = q.popleft()
        print(v, end='')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

bfs(graph, 1, visited)