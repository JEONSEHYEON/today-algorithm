# import sys

# sys.stdin = open('input.txt')

N = int(input())
# print(num)

dp = [0] * (91)

dp[1] = 1
dp[2] = 1
if N >= 3:
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
# print(dp)
print(dp[N])