s = input()
t = input()
n, m = len(s), len(t)
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        # 方法1: s[i]とt[j]が一致する場合
        if s[i] == t[j]:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + 1)
        # 方法2: sのi番目の文字を使わない
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
        # 方法3: tのj番目の文字を使わない
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])
    #print(dp)
res = ""
i, j = n, m
while i > 0 and j > 0:
    # (i-1, j) -> (i, j) と更新されていた場合
    if dp[i][j] == dp[i-1][j]:
        i -= 1
    # (i, j-1) -> (i, j) と更新されていた場合
    elif dp[i][j] == dp[i][j-1]:
        j -= 1
    # (i-1, j-1) -> (i, j) と更新されていた場合
    else:
        res = s[i-1] + res  # このとき s[i-1] == t[j-1]
        i -= 1
        j -= 1
print(res)
