'''
dp[x] = dp[x-1] + 2*dp[x-2]
why? dp[x-1]에는 맨 오른쪽 1x2를 넣는다고 생각
     dp[x-2]에는 맨 오른쪽에 2x2 , 2x1를 넣는다고 생각
'''
n = int(input())
dp = [0,1,3]
for i in range(2, n):
  dp.append((dp[i] + (2*dp[i-1])) % 10007)
print(dp[n])
