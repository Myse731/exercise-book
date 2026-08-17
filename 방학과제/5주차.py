#1번
n = int(input())
nums = []

for i in range(n):
	start, end = map(int, input().split())
	nums.append((start, end))

nums.sort()

for i in range(1, n):
	prev = nums[i-1][1]
	curr_start = nums[i][0]

	if curr_start < prev:
		print("YES")
		break

else:
	print("NO")

#2번
n = int(input())

nums = list(map(int, input().split()))
nums.sort()
idx = 0
hap = 0

for i in nums:
	idx += i
	hap += idx

print(hap)

#3번
n = int(input())

ct1 = 0
ct2 = 0
ct3 = 0
ct4 = 0

ct1 = n // 500 
n %= 500
ct2 = n // 100
n %= 100
ct3 = n // 50
n %= 50
ct4 = n // 10

print(f"{ct1+ct2+ct3+ct4}\n{ct1} {ct2} {ct3} {ct4}")

#4번
n = int(input())

a, b = 0, 1
for i in range(n):
	a, b = b, a+b

print(a)

#5번
n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

for i in range(n-k, n):
	nums[i] = nums[i] // 2

total = 0
for j in nums:
	total += j

print(total)

#6번
