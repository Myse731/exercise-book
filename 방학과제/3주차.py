#1번
n, m = map(int, input().split())
nums = []
for i in range(n):
	nums.append(list(map(int,input().split())))

for i in range(m):
	for j in range(n):
		print(f"{nums[j][i]}", end = ' ')
	print()

#2번
hang, ten = map(int, input().split())
st_x, st_y = map(int, input().split())
wech = input()

for i in wech:
	if(i == 'U'):
		if(st_x - 1 >= 1 and hang >= st_x - 1):
			st_x -= 1
			
	elif(i == 'D'):
		if(st_x + 1 >= 1 and hang >= st_x + 1):
			st_x += 1
			
	elif(i == 'L'):
		if(st_y -1 >= 1 and ten >= st_y -1):
			st_y -= 1
			
	elif(i == 'R'):
		if(st_y + 1 >= 1 and st_y + 1 <= ten):
			st_y += 1


print(f"{st_x} {st_y}")

#3번
m, ya = map(int, input().split())
a, b = map(int, input().split())

for i in range(m):
	if(i == a - 1 or i == b - 1):
		print("X", end = '')
	else:
		print("O", end = '')

#4번
n = int(input())
nums = list(map(int, input().split()))


cur_st = 0
best_st = 0
max_ct = 1
count = 1
for i in range(n-1):
	if nums[i] < nums[i+1]:
		count += 1
	else:
		if(max_ct < count):
			max_ct = count
			best_st = cur_st
		count = 1
		cur_st = i + 1
		
if max_ct < count:
	max_ct = count
	best_st = cur_st
print(f"{best_st+1}")

#5번
n = int(input())

files = []
for i in range(n):
	files.append(input().split('.'))

counts = {}

for j in range(n):
	start = files[j][-1]
	if start in counts:
		counts[start] += 1
	else:
		counts[start] = 1

for i in sorted(counts.keys()):
	print(f"{i} {counts[i]}")

#6번
n = int(input())

scores = {}
for i in range(n):
	name, score = input().split()
	score = int(score)
	scores[name] = score

for i in sorted(scores.keys(), key = lambda x : (-scores[x], x)):
	print(f"{i}")

#7번
n = int(input())

stack = []
result = []
for i in range(n):
	cmd = input().split()
	if(cmd[0] == 'PUSH'):
		stack.append(int(cmd[1]))
	elif(cmd[0] == 'SIZE'):
		result.append(len(stack))
	elif(cmd[0] == 'POP'):
		if not stack:
			result.append(-1)
		else:
			result.append(stack.pop())

for j in result:
	print(f"{j}")

#8번
n =  int(input())
queue = []
result = []

for i in range(n):
	cmd = input().split()
	if cmd[0] == 'PUSH':
		queue.append(cmd[1])
	elif cmd[0] == 'POP':
		result.append(queue.pop(0))
	elif cmd[0] == 'FRONT':
		result.append(queue[0])
	elif cmd[0] == 'SIZE':
		result.append(len(queue))

for i in result:
	print(i)

#9번
count = 0
a = input()

for i in a:
	if(i == '('):
		count += 1
	elif(i == ')'):
		count -= 1
	if count < 0:
		break

if(count == 0):
	print("YES")
else:
	print("NO")

#10번
total = 0
n = int(input())

sold = list(map(int, input().split()))
stack = []

for i in range(n):
	if(sold[i] == 0):
		stack.pop()
	else:
		stack.append(sold[i])

print(sum(stack))

#11번
n = int(input())
stack = []

for i in range(n):
	cmd = input().split()
	if cmd[0] == 'TYPE':
		stack.append(cmd[1])
	elif cmd[0] == 'UNDO':
		stack.pop()

result = ''
for i in stack:
	result += i

print(result)

#12번
n = int(input())
nums = list(map(int, input().split()))

stack_nums = []
sum = 0

for i in nums:
	sum += i
	stack_nums.append(sum)

print(*stack_nums)