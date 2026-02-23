n = int(input())
H = list(map(int,input().split()))

dp = [float("inf")] * n
dp[0] = 0
for i in range(n):
    if i+1 < n:
        dp[i+1] = min(dp[i+1], dp[i] + abs(H[i+1] - H[i]))
    if i+2 < n:
        dp[i+2] = min(dp[i+2], dp[i] + abs(H[i+2] - H[i]))

print(dp[n-1])
