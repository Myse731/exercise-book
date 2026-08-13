#1351번 구구단 출력하기 2 
# a, b = map(int, input().split())

# for i in range(a, b+1):
# 	for j in range(1, 10):
# 		print(f'{i} * {j} = {i * j}')

#1352번 사각형 출력하기 1
# a = int(input())
# for i in range(a):
# 	for j in range(a):
# 		print("*", end = '')
# 	print("")

#1353번 삼각형 출력하기1
# a = int(input())

# for i in range(a):
# 	for j in range(i+1):
# 		print("*", end = '')
# 	print("")

#1354번 삼각형 출력하기2
# a = int(input())

# for i in range(a):
# 	for j in range(a-i):
# 		print("*", end = "")
# 	print("")

#1355번 삼각형 출력하기3
# a = int(input())

# for i in range(a):
# 	for j in range(i):
# 		print(" ", end = "")
# 	for h in range(a - i):
# 		print("*",end = "")
# 	print("")

#1114, 1115
# a, b = map(int, input().split())
# print(a+b)

#1116
# a, b = map(int, input().split())
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a//b}")

#1117
# a, b = map(float, input().split())
# sum = a * b
# print(f"{sum:.2f}")

#1118
# a, b = map(int, input().split())
# nulb = (a * b) / 2
# print(f"{nulb:.1f}")

#1119
# a = int(input())
# print(f"{a * 24}")

#1120
# a, b, c = map(int, input().split())
# avg = (a + b + c) / 3
# print(f"{avg:.2f}")

#1121
# a, b = map(int, input().split())
# print(f"{a%b}")

#1122
# a = int(input())
# bun = a // 60
# cho = a % 60
# print(f"{bun} {cho}")

#1123
# a = int(input())
# hakc = 9 / 5 * a + 32
# print(f'{hakc:.3f}')

#1125
# a = int(input())
# print(f"{a:o} {a:X}")

#1135, 1136, 1137
# a, b = map(int, input().split())
# if(a >= b):
#     print('1')
# else:
#     print('0')

# a, b = map(int, input().split())
# if a == b : 
#     print('1')
# else:
#     print('0')

# a, b = map(int, input().split())
# if a != b : 
#     print('1')
# else:
#     print('0')

#1138, 11139
# a = int(input())
# print(int(not(a)))

# a, b = map(int,input().split())
# print(int(a and b))

# a, b = map(int,input().split())
# print(int(a or b))

#1143, 1144
# a, b = map(int, input().split())
# bit = a & b
# print(f"{int(bit)}")

# a, b = map(int, input().split())
# bit = a | b
# print(f"{int(bit)}")

#1145
# a, b = map(int, input().split())
# shipt = a << b
# print(f"{int(shipt)}")

#1146
# a, b = map(int, input().split())
# shipt = a >> b
# print(f"{int(shipt)}")

#1147
# a, b = map(int, input().split())
# if a > b:
#     print(a)
# else:
#     print(b)

#1148
# a, b, c = map(int,input().split())
# if a <= b and a <= c:
#     print(a)
# elif b <= a and b <= c:
#     print(b)
# else:
#     print(c)

#1153
# a, b = map(int, input().split())
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# elif a == b:
#     print('=')

#1154
# a, b = map(int, input().split())
# if a >= b:
#     print(a - b)
# elif a <= b:
#     print(b - a)

#1155
# a = int(input())
# if a % 7 == 0:
#     print('multiple')
# else:
#     print('not multiple')

# 1156
# a = int(input())
# if a % 2 == 0:
#     print('even')
# else:
#     print('odd')

#1157
# a = float(input())
# if a >= 50 and a <= 60:
#     print('win')
# else:
#     print('lose')

#1158
# a = int(input())
# if a >= 30 and a <= 40:
#     print('win')
# elif a >= 60 and a <= 70:
#     print('win')
# else:
#     print('lose')

#1159
# a = int(input())
# if (a >= 50 and a <= 70) or a % 6 == 0:
#     print('win')
# else:
#     print('lose')

#1160
# a = int(input())
# if a % 2 != 0:
#     print('oh my god')
# else:
#     print('enjoy')

# 1161
# a, b = map(int, input().split())
# if a % 2 == 0 and b % 2 == 0:
#     print('짝수+짝수=',end = '')
# elif a % 2 == 0 and b % 2 != 0:
#     print('짝수+홀수=', end = '')
# elif a % 2 != 0 and b % 2 == 0:
#     print('홀수+짝수=', end = '')
# else:
#     print('홀수+홀수=', end = '')

# sum = a + b
# if sum % 2 == 0:
#     print('짝수')
# else:
#     print('홀수')

#1162
# a, b, c = map(int,input().split())
# sum = a - b + c
# if sum % 10 == 0:
#     print('대박')
# else:
#     print('그럭저럭')

#1163
# y, m, d = map(int,input().split())
# sum = (y+m+d)

# if ((sum / 100) % 10) % 2 == 0:
#     print("대박")
# else:
#     print("그럭저럭")

#오류 수정 1163
# y, m, d = map(int,input().split())
# sum = y + m + d
# result = (sum // 100) % 10

# if result % 2 == 0:
#     print("대박")
# else:
#     print("그럭저럭")

#1164
# car_h = 170

# t1, t2, t3 = map(int,input().split())

# if(car_h < t1 and car_h < t2 and car_h < t3):
#     print('PASS')
# else:
#     print('CRASH')

#1165
# nt, our_sc = map(int,input().split())
# result = our_sc
# i = nt
# while True:
#     result += 1
#     nt += 5
#     if nt >= 90:
#         break
# print(result)

#1166
# y = int(input())

# if(y % 400 == 0):
#     print("Leap")
# elif(y % 4 == 0 and y % 100 != 0):
#     print("Leap")
# else:
#     print("Normal")

#1167
# a, b, c = list(map(int,input().split()))
# minl = min(a, b, c)
# maxl = max(a, b, c)
# sum = a + b + c
# print(sum -(maxl+minl))

#1168
# y, g = map(str,input().split())
# result = 0
# if(g == '1' or g == '2'):
#     result = 1900 + int(y[:2])
#     age = 2012 - result + 1
#     print(age)
# elif(g == '3' or g == '4'):
#     result = 2000 + int(y[:2])
#     age = 2012 - result + 1
#     print(age)

#1169
# age = int(input())
# gender = 0
# if(13 - age >= 0):
#     gender = 3
# else:
#     gender = 1

# y = (2012 - age) + 1
# print(f"{y % 100} {gender}")

#1170
# g, c, n = map(int,input().split())

# if(n >= 10):
#     print(f"{g}{c}{n}")
# else:
#     print(f"{g}{c}0{n}")

#1171
# g, c, n = map(int,input().split())

# 1 1 1, 1 1 2, 1 1 3, 1 2 1, 1 2 2, 1 2 3
# if(c // 10 > 0):
#     if(n >= 100):
#         print(f"{g}{c}{n}")
#     elif(n >=10):
#         print(f"{g}{c}0{n}")
#     else:
#         print(f"{g}{c}00{n}")
   
# else:
#     if(n >= 100):
#          print(f"{g}0{c}{n}")
#     elif(n >=10):
#         print(f"{g}0{c}0{n}")
#     else:
#         print(f"{g}0{c}00{n}")

#1172
# a, b, c = list(map(int,input().split()))

# suml = a + b + c
# maxl = max(a, b, c)
# minl = min(a, b, c)

# mid = suml - (maxl+minl)

# print(f"{minl} {mid} {maxl}")

#1173
# si, bun = map(int,input().split())
# if(si != 0):
#     if(bun >= 30):
#         print(f"{si} {bun - 30}")
#     else:
#         print(f"{si - 1} {(60 + bun) - 30}")
# else:
#     if(bun >= 30):
#         print(f"{si} {bun - 30}")
#     else:
#         print(f"{24 - 1} {(60 + bun) - 30}")

#1175
# n = int(input())

# if(n % 7 == 0 or n % 7 == 6):
#     print("주말")
# else:
#     print("주중")

#1180
# n = int(input())

# result = (n % 100) * 10 + (n // 10)

# result_num = (result * 2) % 100
# print(result_num)

# if(result_num <= 50):
#     print("GOOD")
# else:
#     print("OH MY GOD")

#1201
# n = int(input())

# if(n > 0):
#     print("양수")
# elif(n == 0):
#     print("0")
# else:
#     print("음수")

#1202
# n = int(input())

# if(n >= 90):
#     print("A")
# elif(n >= 80):
#     print("B")
# elif(n >= 70):
#     print("C")
# elif(n >= 60):
#     print("D")
# else:
#     print("F")

#1203
# bmi = int(input())

# if(bmi <= 10):
#     print("정상")
# elif(bmi <= 20):
#     print("과체중")
# elif(bmi > 20):
#     print("비만")

#1204
# n = int(input())
# if((n % 10 == 1 or n % 10 == 2 or n % 10 == 3) and n // 10 == 1 ):
#     print(f"{n}th")

# elif(n % 10 == 1):
#     print(f"{n}st")
# elif(n % 10 == 2):
#     print(f"{n}nd")
# elif(n % 10 == 3):
#     print(f"{n}rd")
# else:
#     print(f"{n}th")

#1205
# n, m = map(int,input().split())

# result = [
# n + m,
# n - m,
# m - n,
# n * m,
# n ** m,
# m ** n
# ]

# if(m != 0):
#     result.append(n / m)
# if(n != 0):
#     result.append(m / n)

# max_value = max(result)
# print(f"{max_value:.6f}")

#1206
# n, m = map(int, input().split())

# if(m % n == 0):
#     print(f"{n}*{m//n}={m}")
# elif(n % m == 0):
#     print(f"{m}*{n//m}={n}")
# else:
#     print("none")

#1207
# yout = list(map(int,input().split()))

# count = 0
# for i in range(4):
#     if(yout[i] == 1):
#         count += 1
# if(count == 0):
#     print("모")
# elif(count == 1):
#     print("도")
# elif(count == 2):
#     print("개")
# elif(count == 3):
#     print("걸")
# elif(count == 4):
#     print("윷")

#1210
# menus = {
#     "치즈버거": 400,
#     "야채버거": 340,
#     "우유": 170,
#     "계란말이": 100,
#     "샐러드": 70
# }

# n, m = map(int, input().split())
# caloy = menus[n] + menus[m]

# if(caloy > 500):
#     print("angry")
# elif(caloy <= 500):
#     print("no angry")

#1212
# a, b, c = map(int, input().split())
# max_n = max(a, b, c)

# sum_n = (a + b + c) - max_n

# if(max_n < sum_n):
#     print("yes")
# else:
#     print("no")

#1214
# y, m = map(int, input().split())
# yun = 0
# if((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)):
#     yun = 1

# if(m <= 7):
#     if(m == 2 and yun == 1):
#         print("29")
#     elif(m == 2 and yun == 0):
#         print("28")
#     elif(m % 2 == 0):
#         print("30")
#     elif(m % 2 != 0):
#         print("31")
# elif(m > 7):
#     if(m % 2 == 0):
#         print("31")
#     else:
#         print("30")

#1216
# a, b, c = map(int, input().split())

# advert_profit = b - c

# if advert_profit > a:
#     print("advertise")
# elif advert_profit < a:
#     print("do not advertise")
# else:
#     print("does not matter")

#1218
# a, b, c = map(int, input().split())
# max_n = max(a, b, c)
# sum_n= a + b + c

# if max_n < (sum_n - max_n):
#     if a == b == c:
#         print("정삼각형")
#     elif a == b or b == c or c == a:
#         print("이등변삼각형")
#     elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
#         print("직각삼각형")
#     else:
#         print("삼각형")
# else:
#     print("삼각형아님")

#1222
# time, score1, score2 = map(int,input().split())

# while True:
#     if(time >= 90):
#         break
#     score1 += 1
#     time += 5

# if(score1 > score2):
#     print("win")
# elif(score1 < score2):
#     print("lose")
# else:
#     print("same")

#1224
# a, b, c, d = map(int, input().split())

# if(a / b  >  c / d):
#     print(">")
# elif(a / b  <  c / d):
#     print("<")
# else:
#     print("=")

#1226
# lotto = list(map(int, input().split()))
# my_lotto = list(map(int, input().split()))

# main_lotto = lotto[:6]

# count = 0
# bonus = 0

# for i in my_lotto:
#     if(i in main_lotto):
#         count += 1

# if(lotto[6] in my_lotto):
#     bonus +=1

# if(count == 6):
#     print("1")
# elif(count == 5 and bonus == 1):
#     print("2")
# elif(count == 5):
#     print("3")
# elif(count == 4):
#     print("4")
# elif(count == 3):
#     print("5")
# elif(count <= 2):
#     print("0")

#1228
# ki, kg = map(float, input().split())

# pyojun = (ki - 100) * 0.9
# biman = (kg - pyojun) * 100 / pyojun

# if(biman <= 10):
#     print("정상")
# elif(biman <= 20):
#     print("과체중")
# elif(biman > 20):
#     print("비만")

#1229
# ki, kg = map(float, input().split())
# pyo = 0

# if(ki < 150):
#     pyo = ki - 100
# elif(ki < 160):
#     pyo = (ki - 150)/2 + 50
# elif(ki >= 160):
#     pyo = (ki - 100) * 0.9
# biman = (kg - pyo) * 100 / pyo

# if(biman <= 10):
#     print("정상")
# elif(biman <= 20):
#     print("과체중")
# elif(biman > 20):
#     print("비만")

#1230
# a, b, c = map(int, input().split())
# if(a <= 170):
#     print(f"CRASH {a}")
# elif(b <= 170):
#     print(f"CRASH {b}")
# elif(c <= 170):
#     print(f"CRASH {c}")
# else:
#     print("PASS")

#1231
# expr = input().strip()

# if '+' in expr:
#     a, b = map(int, expr.split('+'))
#     print(a + b)
# elif '-' in expr:
#     a, b = map(int, expr.split('-'))
#     print(a - b)
# elif '*' in expr:
#     a, b = map(int, expr.split('*'))
#     print(a * b)
# elif '/' in expr:
#     a, b = map(int, expr.split('/'))
#     print(f"{a / b:.2f}")

# #1251
# for i in range(1, 101):
# 	print(f"{i}", end = ' ')

# #1252
# n = int(input())

# for i in range(1, n+1):
# 	print(f"{i}", end = ' ')

# #1253
# a, b, = map(int, input().split())

# if(a > b):
# 	for i in range(b, a+1):
# 		print(f"{i}", end = ' ')
# else:
# 	for j in range(a, b+1):
# 		print(f"{j}", end = ' ')

#1254
# a,b = input().split()
# for i in range(ord(a), ord(b) + 1):
# 	print(f"{chr(i)}", end = ' ')

#1255
# a, b = map(float, input().split())
# while a <= b + 0.0001:
#     print(f"{a:.2f}", end = ' ')
#     a += 0.01

#1256
# n = int(input())
# for i in range(n):
#     print("*", end = '')

#1257
# a, b = map(int, input().split())
# for i in range(a, b +1):
#     if(i % 2 != 0):
#         print(f"{i}", end = ' ')

#1258
# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print(f"{sum}")

#1259
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     if(i % 2 == 0):
#         sum += i
# print(sum)

#1260
# a, b = map(int, input().split())
# sum = 0
# for i in range(a, b+1):
#     if(i % 3 == 0):
#         sum += i
# print(sum)

#1283
# n = int(input())
# m = int(input())
# nums = list(map(int, input().split()))

# result = 0
# tuza = 0

# tuza = float(n)

# for i in range(m):
#     tuza = tuza * (1 + nums[i] / 100)

# result = tuza - n
# last_result = float(f"{result:.0f}")

# if last_result == 0 :
#     print(0)
#     print("same")
# elif last_result > 0:
#     print(f"{result:.0f}")
#     print("good")
# else:
#     print(f"{result:.0f}")
#     print("bad")

#1284
# def is_prime(a):
#     if(a <= 1):
#         return False
#     for i in range(2, int(a**0.5)+1):
#         if(a % i == 0):
#             return False
#     return True

# n = int(input())
# p = 0
# for i in range(2, int(n**0.5)+1):
#     if(n % i == 0):
#         p = i
#         break

# if p == 0:
#     print("wrong number")
# else:
#     q = n//p
#     if(is_prime(p) and is_prime(q)):
#         if(p > q):
#             print(f"{q} {p}")
#         else:
#             print(f"{p} {q}")
#     else:
#         print("wrong number")
    
#1285
# nums = str(input())
# result = 0
# num = 0
# op = '+'

# for i in nums:
#     if i.isdigit():
#         num = num * 10 + int(i)
#     else:
#         if op == '+':
#             result += num
#         elif op == '-':
#             result -= num
#         elif op == '*':
#             result *= num
#         elif op == '/':
#             result //= num

#         op = i
#         num = 0
# print(result)

#1286
# nums = []
# for i in range(5):
#     nums.append(int(input()))

# print(f"{max(nums)}\n{min(nums)}")

#1287
# n = int(input())

# for i in range(1,10):
#     print('*' * (i * n))

#1294
# amho = input()
# cizo = ''
# for i in range(len(amho)):
#     if amho[i] == ' ':
#         cizo += ' '
#     else:
#         bibun = (ord(amho[i]) - ord('a') + 3) % 26 + ord('a')
#         cizo += chr(bibun)
# print(f"{cizo}")
#1675
# amho = input()
# cizo = ''
# for i in range(len(amho)):
#     if amho[i] == ' ':
#         cizo += ' '
#     else:
#         bibun = (ord(amho[i]) - ord('a') - 3) % 26 + ord('a')
#         cizo += chr(bibun)
# print(f"{cizo}")

#5079
# n = int(input())
# topyo = input()
# ct_a = 0
# ct_b = 0
# for i in topyo:
#     if(i == 'A'):
#         ct_a += 1
#     else:
#         ct_b += 1

# if(ct_a > ct_b):
#     print('A')
# elif(ct_a == ct_b):
#     print("Tie")
# else:
#     print('B')

#1261
# n = map(int, input().split())
# for i in n:
#     if(i % 5 == 0):
#         print(i)
#         break
# else:
#     print(0)

#1272
# nums = map(int, input().split())
# result = 0
# for i in nums:
#     if(i % 2 != 0):
#         result += (i+1) // 2
#     else:
#         result += (i // 2) * 10

# print(result)

#1274
# n = int(input())
# is_prime = True

# for i in range(2, n):
#     if(n % i == 0):
#         is_prime = False
#         break
# if is_prime:
#     print("prime")
# else:
#     print("not prime")

#1281
# n, m = map(int, input().split())
# result = 0
# answer = ''
# for i in range(n, m+1):
#     if i == n:
#         if(i % 2 == 0):
#             result -= i
#             answer += '-' + str(i)
#         else:
#             result += i
#             answer += str(i)
#     else:
#         if(i % 2 == 0):
#             result -= i
#             answer += '-' + str(i)
#         else:
#             result += i
#             answer += '+' + str(i)
# print(f"{answer}={result}")

#1282
# n = int(input())

# t = int((n - 1) ** 0.5)

# k = n - (t ** 2)

# print(k, t)

#1357
# n = int(input())
# h = 2 * n - 1
# count = 1
# for i in range(1, n+1):
#     print("*" * i)
# for j in range(n-1, 0, -1):
#     print("*" * j)

#1358
# n = int(input())
# h = (n//2)+1
# for i in range(h):
#     space = (n//2) - i
#     star = (2*i) + 1
#     print(" " * space + "*" * star)

#1361
# n = int(input())
# for i in range(n):
#     if(n == 1):
#         print("**")
#         break
#     print(' ' * i, end = '')
#     print("**")

#1365
# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if i == 1 or i == n or j == 1 or j == n or i + j == n + 1 or i == j:
#             print("*", end = '')
#         else:
#             print(" ", end = '')
#     print()

#1367
# n = int(input())
# for i in range(n):
#     print(' ' * (n - 1 - i), end = '')
#     print("*" * n)

#1368
# h, k, lr = input().split()
# h = int(h)
# k = int(k)
# if lr == 'L':
#     for i in range(h):
#         print(' ' * i + '*' * k)
# elif lr == 'R':
#     for j in range(h):
#         print(' ' * (h - 1 - j) + '*' * k)

#1370
# h, r = map(int, input().split())
# for i in range(r):
#     for j in range(h):
#         print(' ' * j + '*')
#     for k in range(h-2, -1, -1):
#         print(' ' * k + '*')

#1371
# n = int(input())
# h = n * 2
# for i in range(1, h + 1):
#     for j in range(1, h +1):
#         if i + j == n + 1:
#             print("*", end = '')
#         elif j - i == n:
#             print("*", end = '')
#         elif i - j == n:
#             print("*", end = '')
#         elif i + j == 3 * n + 1:
#             print("*", end = '')
#         else:
#             print(' ', end = '')
#     print()

#1380
# n = int(input())
# for i in range(1, 7):
#     for j in range(1, 7):
#         if i + j == n:
#             print(f"{i} {j}")

#3122
# n = int(input())

# for i in range(n):
#     space = ' ' * (n - 1 - i)
#     stars = '*' * (2 * i + 1)
#     print(space+stars+space)

# for j in range(n-2, -1, -1):
#     space = ' ' * (n - 1 - j)
#     stars = '*' * (2 * j + 1)
#     print(space+stars+space)

#1677
# w, h = map(int, input().split())

# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         if (i == 1 or i == h) and (j == 1 or j == w):
#             print('+', end='')
#         elif i == 1 or i == h:
#             print('-', end='')
#         elif j == 1 or j == w:
#             print('|', end='')
#         else:
#             print(' ', end='')
#     print()

