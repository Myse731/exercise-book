#1번
n = int(input())

id_list = []
count = 0

for i in range(n):
	id = input()
	if(id not in id_list):
		id_list.append(id)
		count += 1

print(count)
for j in range(count):
	print(f"{id_list[j]}", end = ' ')

#2번
n = int(input())

nums = []

nums = list(map(int,input().split()))

maxi = max(nums) + 1
							
for j in range(1, maxi):
	count = 0
	for k in range(n):
		if(j == nums[k]):
			count += 1
	print(f"{j} {count}")

#3번
n = int(input())
days = list(map(int,input().split()))

len = 0
start = 0
end = 0

count = 0
s_start = 0

for i in range(1, n+1):
	day = days[i - 1]

	if(day == 1):
		if(count == 0):
			s_start = i
		count += 1

		if(len < count):
			len = count
			start = s_start
			end = i
			
	else:
		count = 0

if(len == 0):
	print("0 0 0")
else:
	print(f"{len} {start} {end}")

#4번
n, kijun = map(int, input().split())

scores = {}

for i in range(n):
	name, score = input().split()
	scores[name] = int(score)

count = 0
namse = []

for name, score in scores.items():
	if score >= kijun:
		count += 1
		namse.append(name)

print(f"{count}")
for name in namse:
	print(f"{name}", end = ' ')

#5번
n = int(input())

products = {}

for i in range(n):
	p_name, price = input().split()
	products[p_name] = price

q = int(input())
quetions = []

for j in range(q):
	quetion = input()
	quetions.append(quetion)

for k in quetions:
	if(k in products):
		print(products[k])
	else:
		print("-1")

#5번 더 간단한 버전
n = int(input())
products = {}

for _ in range(n):
    p_name, price = input().split()
    products[p_name] = price

q = int(input())

for _ in range(q):
    query = input()
    print(products.get(query, "-1"))

#6번
n = int(input())

teams = {}

for i in range(n):
	team, score = input().split()
	score = int(score)

	if team in teams:
		teams[team] += score
	else:
		teams[team] = score

for team, score in sorted(teams.items()):
	print(f"{team} {score}")

#7번
n = int(input())

nums1 = set(input().split())

m = int(input())
nums2 = set(input().split())

result = sorted(nums1 & nums2)

print(len(result))
print(*result)

#8번
n = int(input())

nums = list(map(int,input().split()))
result = []

for i in nums:
	if(i not in result):
		result.append(i)

result = sorted(result)

print(*result)

#9번
n = int(input())

nums = {}

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_0 = 0

for i in range(n):
	x, y = map(int,input().split())
	if(x > 0 and y > 0):
		count_1 += 1
	elif(x < 0 and y > 0):
		count_2 += 1
	elif(x < 0 and y < 0):
		count_3 += 1
	elif(x > 0 and y < 0):
		count_4 += 1
	else:
		count_0 += 1

print(f"{count_1} {count_2} {count_3} {count_4} {count_0}")

#10번
n = int(input())

events = []

for i in range(n):
	name, month, day = input().split()
	events.append((int(month), int(day), name))

result = []
events = sorted(events)

for month, day, name in events:
	result.append(name)

print(*result)

#11번
n, m = map(int,input().split())

up = 1

nums = []
num_sum = []

for i in range(n):
	nums = list(map(int, input().split()))

	num_sum.append(sum(nums))
	

print(*num_sum)

#12번
n, m = map(int,input().split())

nums = []
sums = [0] * m

for i in range(n):
	nums = list(map(int, input().split()))
	for j in range(m):
		sums[j] += nums[j]

print(*sums)