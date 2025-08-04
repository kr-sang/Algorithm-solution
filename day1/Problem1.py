import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

# 노드, 간선 수 입력 후 시작 노드 입력
n,m = map(int, input().split())
start = int(input())

# 각 노드별 연결노드 및 가중치 처리
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

#최단거리 테이블 초기화
distance = [INF] * (n+1)

# 다익스트라 알고리즘
def dijkstra(start):
    q = [] # 큐 쓸거니까 그냥 []로 초기화...
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        #아래까지 다 보면 dist는 결국 기존 push된 cost니까 현재 노드까지의 최적 거리를 뜻함.
        dist, now = heapq.heappop(q)
        # 이미 이 경로보다 최적화된 경로가 있다면 pass
        if distance[now] < dist:
            continue
        
        for neighbor, weight in graph[now]:
            cost = dist + weight
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                
                heapq.heappush(q, (cost, neighbor))

dijkstra(start)

for i in range(1,n+1):
    if(distance[i] == INF):
        print("INFINITE")
    else:
        print(distance[i]) # Python은 %d가 필요없구나...
