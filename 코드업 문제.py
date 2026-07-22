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

##1163
y, m, d = map(int,input().split())
sum = (y+m+d)

if ((sum / 100) % 10) % 2 == 0:
    print("대박")
else:
    print("그럭저럭")

##오류 수정 1163
y, m, d = map(int,input().split())
sum = y + m + d
result = (sum // 100) % 10

if result % 2 == 0:
    print("대박")
else:
    print("그럭저럭")