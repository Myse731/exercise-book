#1
num, start, end = map(int,input().split())

high = 0
low = 0

ondo = map(int, input().split())

for i in ondo:
	if i > end:
		high += 1
	elif i < start:
		low += 1
		
print(f"{low} {high}")

#2
num, sanghan = map(int, input().split())

td_money = map(int,input().split())

hap = sum(td_money)

print(f"{sanghan} {hap - sanghan}")

#3
h, w, num = map(int,input().split())

height = 0
result = 0

found = False

for i in range(h):
	width = 0
	height += 1
	for j in range(w):
		width += 1
		result += 1
		if(result == num):
			found = True
			break
	if found:
		break

print(f"{height} {width}")

#4
munza = input()

current_char = munza[0]
count = 0

for char in munza:
	if char == current_char:
		count += 1
	else:
		print(f"{current_char}{count}", end = ' ')
		current_char = char
		count = 1

print(f"{current_char}{count}", end = ' ')

#5
n, k = map(int, input().split())

nums = list(map(int, input().split()))

count = 0

for i in nums:
	if(i % k == 0):
		count += 1
print(count)

#6
num = int(input())

nums = list(map(int, input().split()))

plus = 0
minus = 0
zero = 0

for i in nums:
	if(i == 0):
		zero += 1
	elif(i > 0):
		plus += 1
	else:
		minus += 1

print(f"{plus} {minus} {zero}")

#7
num = int(input())

nums = []
odd = 0
even = 0

nums = list(map(int,input().split()))

for j in nums:
	if(int(j) % 2 == 0):
		even += int(j)
	else:
		odd += int(j)

print(f"{even} {odd}")

#8
munza = input()

moeum = ['a', 'e', 'i', 'o', 'u']
count = 0

for i in munza:
	if(i in moeum):
		count += 1
print(count)

#9
munza = input()

yaru = input()
count = 0

for i in munza:
	if(i == yaru):
		count += 1

print(count)

#10
num = int(input())

max = 0
max_c = ''

for i in range(num):
	munza = input()
	count  = len(munza)
	if(count >= max):
		max = count
		max_c = munza

print(f"{max_c} {max}")

#11
num = int(input())

max = 0
max_n = 0

for i in range(1, num+1):
	score = int(input())
	if(score > max):
		max = score
		max_n = i
		
print(f"{max} {max_n}")

#12
num = int(input())

avg = 0
scores = []

for i in range(num):
	score = int(input())
	scores.append(score)

avg = sum(scores) / num
count = 0

for j in scores:
	if(j > avg):
		count += 1

print(count)
