#기본-팩토리얼
def fac(n):
  sum = 1
  for i in range(1, n+1):
    sum *= i
  return sum

print("팩토리얼 계산")
n = int(input('n 입력 : '))
res = fac(n)
print(f"{n}!={res}")

#재귀-팩토리얼
def fac(n):
  if n == 1:
    return 1
  return fac(n-1) * n

print("팩토리얼 계산")
n = int(input('n 입력 : '))
res = fac(n)
print(f"{n}!={res}")

#일반-피보나치
def fib(n):
  if n <= 0:
    return []
  if n == 1:
    return [1]
  fibo = [1, 1]
  for i in range(2, n):
      fibo.append(fibo[i-1] + fibo[i-2])
  return fibo

print("피보나치 수열")
n = int(input("출력 항의 개수 입력 : "))
print(fib(n))

#재귀-피보나치
