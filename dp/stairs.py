n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])


# 계단오르기
# dp[k]를 구하기 위해서는 dk[k-3]까지 최적이라고 생각하고 그뒤 XOO가 오던지
# 혹은 dp[k-2]까지의 값에서 XO가 오던지밖에 없다. 이유는 마지막 계단은 꼭 밟아야 한다고 가정하면
# OOO가 불가능하고, 이는 dp[k-1]+s[i]를 고려할 수 없는 이유가 된다. 그렇다면 마지막 계단을 기준으로
# 그 앞에 건너뛰던지 그 앞앞에 건너뛰던지의 경우밖에 없고 이는 3칸을 단위로 dp가 가능하게 된다. 대단하네.....