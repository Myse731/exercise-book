#1번
n, m = map(int, input().split())
nums = list(map(int, input().split()))

result = []
for i in range(m):
	hap = 0
	cmd = input().split()
	for j in range(int(cmd[0]), int(cmd[1]) + 1):
		hap += nums[j - 1]
	result.append(hap)

for i in result:
	print(i)

#2번
n = int(input())
nums = list(map(int, input().split()))
m = int(input())
qt = list(map(int, input().split()))
result = []

for i in qt:
	count = 0
	for j in nums:
		if(i == j):
			count += 1
	result.append(count)

for k in result:
	print(k, end= ' ')

#3번
n, m = map(int, input().split())
nums = []
add = 1
for i in range(n):
	row = []
	for j in range(m):
		row.append(add)
		add += 1
	nums.append(row)

hap = 0
for i in range(n):
	for j in range(m):
		if(i == 0 or i == n - 1 or j == 0 or j == m - 1):
			hap += nums[i][j]

print(hap)

#4번
n = int(input())
nums = list(map(int, input().split()))
result = []

for i in range(n):
	if i == 0:
		new = nums[i] + 0 + nums[i + 1]
	elif i  == n - 1:
		new = nums[i] + nums[i - 1] + 0
	else:
		new = nums[i] + nums[i - 1] + nums[i + 1]
	result.append(new)

print(*result)

#5번
n = int(input())
nums = list(map(int, input().split()))
max_result = []

max = 0
for i in nums:
	if(max <= i):
		max = i
	max_result.append(max)

print(*max_result)

#6번
n, m = map(int, input().split())
nums = list(map(int, input().split()))

sum_list = [0] * (n+1)

for i in range(n):
	sum_list[i + 1] = nums[i] + sum_list[i]

result = []
for j in range(m):
	a, b = map(int, input().split())
	hap = sum_list[b] - sum_list[a - 1]
	result.append(hap)

for k in result:
	print(k)

#7번
n = int(input())
nums = list(map(int, input().split()))
q = int(input())
qt = list(map(int, input().split()))

for i in qt:
	if(i in nums):
		print("YES")
	else:
		print("NO")

#8번
n = int(input())
nums = list(map(int, input().split()))
q = int(input())
qt = list(map(int, input().split()))

indx = {}
for i in range(n):
	indx[nums[i]] = i + 1

result = []
for j in qt:
	if j in indx:
		result.append(indx[j])
	else:
		result.append(-1)
print(*result)

#9번
n = input()
q = int(input())

first = {}
for i in range(len(n)):
	char  = n[i]
	if char not in first:
		first[char] = i + 1

for j in range(q):
	cmd = input()
	if cmd in first:
		print(first[cmd])
	else:
		print(-1)

#10번
n, m = map(int, input().split())
nums = list(map(int, input().split()))

m = m % n
new_nums = nums[-m:] + nums[:-m]

print(*new_nums)

#11번
n = int(input())
add = 1
cards = []
for i in range(n):
	cards.append(add)
	add += 1

while len(cards) != 1:
	cards.pop(0)
	nc = cards.pop(0)
	cards.append(nc)

print(*cards)

#11번 수정버전
n = int(input())
add = 1
cards = []
for i in range(1, n + 1):
	cards.append(i)

while len(cards) != 1:
	cards.pop(0)
	cards.append(cards.pop(0))

print(*cards)

#12번
n = int(input())
nums = []
result = []
for i in range(n):
	cmd = int(input())
	if(cmd == 0):
		if(len(nums) == 0):
			result.append(-1)
		else:
			result.append(nums.pop(0))
	else:
		nums.append(cmd)

for j in result:
	print(j)