# 3차 시도
import sys
from collections import deque
input = sys.stdin.readline
dirs = [(-1,0), (1,0), (0,-1), (0,1)]
# 경계 쓰는 함수 대충 하나 만들고
def in_bound(x,y,N):
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False
# 연결노드 덩어리 수 출력 함수 만들고(visited 2중리스트, deque, count반환)
def num_SSC(world):
    visited = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if world[i][j] == "#" and visited[i][j] == False:
                count += 1
                q = deque([(i,j)])#[] 빼먹음. 꼭 써야하나?
                visited[i][j] = True
                while q:
                    y,x = q.popleft()
                    for dx,dy in dirs:
                        cx,cy = x + dx, y + dy
                        if in_bound(cx,cy,len(world[0])) :
                            if visited[cy][cx] == False and world[cy][cx] == "#":
                                q.append((cy,cx))#() 하나 빼먹음. 꼭 써야하나?
                                visited[cy][cx] = True
    return count
# 노드 개수 - 1 = 간선 수 체크 & dfs 돌려서 연결덩어리 체크 함수 만들고
# (노드리스트, edge_set, visited set, dfs)
def tree_check(world, N):
    nodes = []
    for i in range(N):
        for j in range(N):
            if world[i][j] == "#":
                nodes.append((i,j))
    node_count = len(nodes)
    edge_set = set()
    for i,j in nodes:
        for di,dj in dirs:
            ni,nj = i + di, j + dj
            if in_bound(ni,nj,N) and world[ni][nj] == "#":
                a,b = (i,j), (ni,nj)
                if a>b:
                    a,b = b,a
                edge_set.add((a,b))
    edge_count = len(edge_set)
    if edge_count != node_count - 1:
        return False
    visited = set()
    def dfs(i,j):
        visited.add((i,j))
        for di, dj in dirs:
            ni,nj = i + di, j + dj
            if in_bound(ni,nj,N) and world[ni][nj] == "#" and (ni,nj) not in visited:
                dfs(ni,nj)
    dfs(nodes[0][0], nodes[0][1])
    return len(visited) == node_count

# 입력 받고 함수들 써서 결과내기
N=int(input())
choco = [list(map(str,input().strip())) for _ in range(N)]
answer = []
for i in range(N):
    for j in range(N):
        if choco[i][j] == "#":
            choco[i][j] = "."
            if num_SSC(choco) == 1 and tree_check(choco, N):
                answer.append((i+1,j+1))
            choco[i][j] = "#"
print(len(answer))
answer.sort()
for i,j in answer:
    print(i, j)
