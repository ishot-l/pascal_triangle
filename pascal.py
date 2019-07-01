# パスカルの三角形でcombinationをつくる

dp = [[1]]
height = 10

# pascal
for n in range(1,height):
    row = []
    for k in range(n+1):
        if k-1 < 0:
            row.append(dp[n-1][k])
        elif k > n-1:
            row.append(dp[n-1][k-1])
        else:
            row.append(dp[n-1][k-1] + dp[n-1][k])
    dp.append(row)
            
for i in range(height):
    print(" ".join(map(str,dp[i])))
