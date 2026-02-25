n, W = map(int, input().split())
items = []
for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

# 価値の最大値
MAX_V = 100000  # 10^5

# dp[i][v] = i個目まで見て、価値vを得るための最小重さ
dp = [[float('inf')] * (MAX_V + 1) for _ in range(n + 1)]
dp[0][0] = 0  # 0個で価値0を得る重さは0

for i in range(n):
    w, v = items[i]
    for j in range(MAX_V + 1):
        # i個目を入れない
        dp[i+1][j] = dp[i][j]
        
        # i個目を入れる
        if j >= v:
            dp[i+1][j] = min(dp[i+1][j], dp[i][j-v] + w)

# dp[n][v] <= W となる最大のvを探す
ans = 0
for v in range(MAX_V + 1):
    if dp[n][v] <= W:
        ans = v

print(ans)
