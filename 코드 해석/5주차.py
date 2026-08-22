#6번
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

#7번
n, m = map(int, input().split())
coins = list(map(int, input().split()))

dp = [1001] * (m + 1)

dp[0] = 0

for coin in coins:
    for i in range(coin, m + 1):
        if dp[i - coin] + 1 < dp[i]:
            dp[i] = dp[i - coin] + 1

if dp[m] == 1001:
    print(-1)
else:
    print(dp[m])

#8번
n, m, s = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
visited[s] = True

queue = [s]
count = 0

while queue:
    current = queue.pop(0)
    
    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)
            count += 1

print(count)

#9번
n, m, a, b = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [-1] * (n + 1)
visited[a] = 0

queue = [a]

while queue:
    current = queue.pop(0)
    
    if current == b:
        break
        
    for neighbor in graph[current]:
        if visited[neighbor] == -1:
            visited[neighbor] = visited[current] + 1
            queue.append(neighbor)

print(visited[b])

#10번
N, K = map(int, input().split())

results = []
current = []

def dfs(start):
    if len(current) == K:
        results.append(list(current))
        return
    
    for i in range(start, N + 1):
        current.append(i)
        dfs(i + 1)
        current.pop()

dfs(1)

print(len(results))

for comb in results:
    print(*comb)

#11번
n = int(input())

nums = list(map(int, input().split()))

if n == 1:
	print(*nums)
else:
	while len(nums) > 1:
		next_round = []
		for i in range(0, len(nums), 2):
			if nums[i] > nums[i+1]:
				next_round.append(nums[i])
			else:
				next_round.append(nums[i+1])

		print(*next_round)
		nums = next_round

#12번
