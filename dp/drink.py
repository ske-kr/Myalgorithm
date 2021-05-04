n=int(input())

alcohol=[0]
dp=[0]
for i in range(n):
    alcohol.append(int(input()))

dp.append(alcohol[1])

if n>=2:
    dp.append(alcohol[1]+alcohol[2])

if n>=3:
    for i in range(3,n+1):
        dp.append(max(dp[i-3]+alcohol[i-1]+alcohol[i],dp[i-2]+alcohol[i],dp[i-1]))

print(dp[n])
#stair와 상당히 비슷하지만 차이점은 stair는 마지막계단을 밟아야함
#포도주는 마지막계단을 밟아야할 이유가 없음
# 그러므로 포도주는 고려해야할 대상이 XOO XO X 3가지를 고려해야 한다
# 차이점에 유의하자
#첫번째값을 0넣어주는거 잊지말기;ㅅㅂ