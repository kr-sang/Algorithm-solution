import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
# 입력받은 input의 첫 줄을 map 형태로 load
n,m = map(int, (input().split()))
# 이중 list를 통해 각 노드별 연결선 및 가중치 지정 준비
graph = [[] for _ in range(n+1)]

# 이제 입력을 전부 받아와서, 양방향으로 노드 연결해주기.(양방향이 중요)
for _ in range(m):
    a,b,c = map(int, (input().split()))
    graph[a].append((b,c))
    graph[b].append((a,c))

# 여우와 늑대 각각에 대해 해당 노드까지의 최소가중치 계산 준비. 늑대는 state를 고려하여 이중 list.
dist_fox = [INF] * (n+1)
dist_wolf = [[INF]*2 for _ in range (n+1)]

def dijkstra():
    q_fox = []
    q_wolf = []
    heapq.heappush(q_fox, (0, 1))
    heapq.heappush(q_wolf, (0, 1, 0))
    dist_fox[1] = 0
    # 늑대의 첫 노드에서는 state가 0이어야 하므로 1일 때를 INF로 나누어 금지시킴
    dist_wolf[1][0] = 0
    dist_wolf[1][1] = INF
    
    # 여우는 다익스트라 알고리즘 그대로 활용.
    while q_fox:
        distance, now = heapq.heappop(q_fox)
        if distance > dist_fox[now]:
            continue
        for destination, weight in graph[now]:
            cost = dist_fox[now]+weight
            if dist_fox[destination] > cost:
                dist_fox[destination] = cost
                heapq.heappush(q_fox, (cost, destination))

    # 늑대는 state를 추가해줌. 현재 노드와 연결된 노드에 대하여 
    # 현재 노드에 도달할 때의 state를 기준으로 결과를 내도록 설정함.
    while q_wolf:
        distance, now, temp = heapq.heappop(q_wolf)
        if distance > dist_wolf[now][temp]:
            continue
        for destination, sub_weight in graph[now]:
            if temp == 0:
                weight = float(sub_weight)/float(2)
                
            else :
                weight = sub_weight * 2
            #다음 state를 toggle을 통해 지정.
            next_temp = temp ^ 1        
            cost = weight + distance
            if dist_wolf[destination][next_temp] > cost:
                dist_wolf[destination][next_temp] = cost
                heapq.heappush(q_wolf, (cost, destination, next_temp))
    # 결과를 출력하는 부분. 사실 이 부분은 dijkstra()함수 밖으로 나가도 된다.
    result_wolf = [INF]*(n+1)
    result = 0
    for i in range(1,n+1):
        result_wolf[i] = min(dist_wolf[i][0], dist_wolf[i][1])
        
        if dist_fox[i] < result_wolf[i]:
            result += 1
    print(result)



dijkstra()
