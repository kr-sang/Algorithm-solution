import sys
#첫 줄에 물품 수 N과 버틸 무게 K가 주어짐
#그 다음 N개의 줄에 무게 W와 가치 V가 주어짐
#이를 토대로 냅색 문제 해결.

#입력 받아오기
input = sys.stdin.readline
#받아온 입력 NK 처리
N, K = map(int, input().split())#이렇게 쓰는게 맞았나?
#받아온 입력 N개 줄 무게가치 처리
stuff = [[0,0] for _ in range (N+1)] # [0,0]과 [0]*2가 차이가 있는지 확인하자.
for i in range(1, N+1): # 파이썬에서 for문은 1이상 N+1 '미만'으로 해석된다.
    stuff[i][0], stuff[i][1] = map(int, input().split())
# dp[i][j]  = max(dp[i-1][j], dp[i-1][j-current_w]) 루프 돌리기
dp = [[0] * (K+1) for _ in range (N+1)] 
for i in range (1, N+1):
    for j in range (1, K+1):
        if j >= stuff[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-stuff[i][0]]+stuff[i][1])
        else:
            dp[i][j] = dp[i-1][j]
# 그렇게 나온 마지막 요소 dp[N][K] 출력.
print(dp[N][K])
