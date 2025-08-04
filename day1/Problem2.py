import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
#몇 번째 world 입력인지 알기 위해 cnt 지정
cnt = 0

while N != 0:
    cnt += 1
    #기본 world, 최단queue, 해당 좌표까지의 최소거리 설정
    world = [list(map(int, input().split())) for _ in range (N)] # [int(input().split())]으로 쓰면 안됨.
    q = []
    dist = [[INF]*N for _ in range (N)]
    #초기지점 설정 후 push.
    dist[0][0] = world[0][0]
    heapq.heappush(q, (world[0][0], 0, 0))
    while q:
        weight, y, x = heapq.heappop(q)
        # destination 도달 시.
        if y == N-1 and x == N-1:
            print("Problem", str(cnt)+":", weight)
            N = int(input())
            break
        for i in range (4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<=N-1 and 0<=ny<=N-1:
                cost = world[ny][nx] + weight # weight 자체에 이미 이전 cost가 들어있기 때문에 world[ny][nx]만 더해주면 된다.
                if cost < dist[ny][nx]:
                    dist[ny][nx] = cost
                    heapq.heappush(q, (cost, ny, nx))
