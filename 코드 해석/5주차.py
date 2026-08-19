n = int(input())

if n == 1:
	print(1)
elif n == 2:
	print(2)
else:
	a, b = 1, 2
	for i in range(3, n+1):
		a, b = b, a+b

print(b) #=> 아직 잘 모르겠음

# 1. 동전 종류 수(N)와 목표 금액(M) 입력 받기
n, m = map(int, input().split())

# 2. 동전 금액 목록 입력 받기
coins = list(map(int, input().split()))

# 3. DP 테이블 초기화
# M원을 포함해야 하므로 (M + 1) 크기로 만들고, 나올 수 없는 큰 값(1001)으로 채움
dp = [1001] * (m + 1)

# 0원을 만드는 데 필요한 동전 개수는 0개
dp[0] = 0

# 4. 각 동전별로 표(DP 테이블) 채우기
for coin in coins:
    for i in range(coin, m + 1):
        # 기존 개수 vs (i - coin)원을 만든 개수 + 1 중 더 작은 값 선택
        if dp[i - coin] + 1 < dp[i]:
            dp[i] = dp[i - coin] + 1

# 5. 결과 출력
# dp[m]이 1001 그대로라면 M원을 만들 수 없는 경우임
if dp[m] == 1001:
    print(-1)
else:
    print(dp[m])