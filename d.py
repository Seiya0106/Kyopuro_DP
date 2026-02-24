n, w = map(int,input().split())
W = []
V = []
for _ in range(n):
    wt, va = map(int,input().split())
    W.append(wt)
    V.append(va)

dp = [[0] * (w+1) for _ in range(n+1)]
# i個目まで見て重さjにまで使った時の最大価値
for i in range(n):
    for j in range(w+1):
        if j >= W[i]:
            dp[i+1][j] = max(dp[i][j], dp[i][j-W[i]] + V[i])
        else:
            dp[i+1][j] = dp[i][j]
    print(dp)
print(dp[n][w])
