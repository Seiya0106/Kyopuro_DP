n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = a[0]

for i in range(1, n):
    for j in range(3): # 今日の活動
        for k in range(3): # 昨日の活動
            if j != k:
                dp[i][j] = max(dp[i][j], dp[i-1][k] + a[i][j])
        print(dp)

# print(dp)
print(max(dp[n-1]))
