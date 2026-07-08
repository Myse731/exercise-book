# a = 2

# a = a ** 2

# print(a)

# #문제3
# a, b = map(int,input().split())
# tmp = a
# a = b
# b = tmp
# print(a,b)

# #문제2
# a = input()
# b = 0
# for i in a:
#    b += int(i)
# print(b)

# a = 123
# one = a % 10
# a = a // 10

# two = a % 10
# a = a // 10

# three = a % 10
# a = a // 10

# print(one + two + three)

# #문제1
# a = int(input())

# a = 9
# print(bin(a))#bin == binary의 약자

# a = 3

# b = 2
# #복합 대입 연산자
# # a += b
# # a -= b
# # a *= b
# # a /= b
# # a //= b
# # a %= b

# #비교 연산자
# # print(a == b)
# # print(a != b)
# # print(a > b)
# # print(a >= b)
# # print(a < b)
# # print(a <= b)

# x = 'SKSAMSUNG'
# print(x[0:2],x[2:])

# #3주차 1차시 인덱싱 연습
# a = 010-1234-5678
# print

# #3주차 1차시 인덱싱 연습
# file_name = "report.pdf"
# print(file_name[:6]+".png")

# #3주차 1차시 인덱싱 연습a = "010-1234-5678"
# a1 = a.replace("1234","****")
# print(a1)
# print(a[:4]+"****"+a[8:])

# #3주차 1차시 인덱싱 연습
# a = "01012345678"
# print(a[:3]+"-"+a[3:7]+"-"+a[7:])

# card_number = "1234-5678-9012-3456"
# s= '****'

# print(f"결제카드:{s}-{s}-{s}{card_number[14:]}")

# #메서드 체이닝

# url = "  www.NAVER.com/blog  "


# print(f"연결주소:{url.strip()[:-5].lower().replace("www.", "https://")}")

# raw_name = " P ark gu n woo"
# print(f"성: {raw_name.upper().replace(' ','')[:4]} / 이름: {raw_name.upper().replace(' ','')[-6:]}")

# file_info = "20260316_test_report.pdf"
# print(f"작성일 : {file_info[:4]}년 {file_info[5:6]}월 {file_info[6:8]}일")
# print(f"확장자 : {file_info[21:].upper()} 문서")

# raw_data = "  2024-03-16  "
# print(f"{raw_data.strip()[:4]}년")

# # a = 10
# # b = 2
# # print(a & 1 == 0) 짝수 판별
# n = int(input())
# print(n & (n-1) == 0)

# a = input()
# print(f"{a[:2]}{a[-2:]}")

# a = input()
# b = input()

# print(f"{a[0]}+{b[::]}+{a[1]}")

# a = input()
# print(f"{'입력값 :'}{a}")
# if a == a[::-1]:
#   print(f"{a}{"는 펠린드롬인가요?"} {True}")
# else:
#   print(f"{False}")

# print(f"{(a := input())}, {a == a[::-1]}")

# a = int(input())
# if a >= 90:
#   print("A")
# elif 89>= a >= 80:
#   print("B")
# elif 79 >= a >= 70:
#   print("C")
# else:
#   print("F")

# a,b,c = map(int, input().split())

# print(max(a, b, c))

# m = int(input())
# name = "부자" if m >= 50000 else"거지"
# ##name = "부자" if m >= 50000 else("중산층" if m >= 30000 else "거지")
# print(name)

# a = input()
# b = input()

# if a == b:
#   result = '비겼습니다'
# elif (a == '가위' and b == '보') or (a == '바위' and b == '가위') or (a == '보' and b == '가위'):
#   result = 'a가 이겼습니다.'
# else :
#   result = 'b가 이겼습니다.'

# print(f'a : {a} , b : {b} , {result}')


# a = input()
# if a.islower() == True:
#   print(a.upper())
# else :
#   print(a.lower())

# alp = 'abcdefghijklmnopqrstuvwxyz'

# num = int(input())

# txt = str(input())

# for i in range(len(txt)):
#   print(  alp[   (alp.find(txt[i]) + num) % 26  ], end='')

# # 후위 표기 코드

# txt = input()

# stack = []

# #첫 문자열이 숫자 -> append()
# for i in range(len(txt)):

#   if txt[i] != '+' and txt[i] != '-' and txt[i] != '*' and txt[i] != '/' :
#     stack.append(int(txt[i]))
#   else :
#     op1 = stack.pop()
#     op2 = stack.pop()
#     if txt[i] == '+':
#       stack.append(op2 + op1)
#     elif txt[i] == '-':
#       stack.append(op2 - op1)
#     elif txt[i] == '*':
#       stack.append(op2 * op1)
#     else:
#       stack.append(op2/ op1)

# print(stack.pop())

# # 괄호 검사 코드

# txt = input()
# stack = []
# checked = True

# for i in txt:
#   if i == '(' or i == '[' or i == '{':
#     stack.append(i)
#   else :
#     if len(stack) == 0 :
#       checked = False
#       break

#     atp = stack.pop()

#     if atp != '(' and atp != '[' and atp != '{' :
#       checked = False
#       break

# if len(stack) != 0:
#   checked = False

# if checked == False:
#   print('에러')
# else :
#   print('통과')

# #합집합
# a = ['아이스크림','떡볶이','스시']

# b = ['국밥', '라면', '아이스크림']

# c = []

# for i in a + b:
#   if i not in c:
#     c.append(i)

# print(c)

# #교집합
# a = ['아이스크림','떡볶이','스시']

# b = ['국밥', '라면', '아이스크림']

# c = a[:]

# for i in c:
#   if i not in b:
#     a.remove(i)

# print(a)

# #차집합
# a = ['아이스크림','떡볶이','스시']

# b = ['국밥', '라면', '아이스크림']

# c = a[:]

# for i in c:
#   if i in b:
#     c.remove(i)

# print(c)

# #대칭 차집합
# a = ['아이스크림','떡볶이','스시']

# b = ['국밥', '라면', '아이스크림']

# c = b[:]

# for i in a:
#   if i not in b:
#     c.append(i)
#     continue
#   if i in b:
#     c.remove(i)

# print(c)

# #대칭 차집합
# a = ['아이스크림', '떡볶이', '스시']

# b = ['국밥', '라면', '아이스크림']


# c = a[:]

# d = b[:]

# for i in c :
#   if i in b:
#     c.remove(i)
# print(c)



# for i in d :
#   if i in a:
#     d.remove(i)
# print(d)


# print(c + d)

# # todo 1 : 반복문을 활용하여 입력받은 값을 5번 출력해 봅시다.
# a = input()
# for i in range(4):
#   print(a)

# # todo 2 : 정수 하나를 입력받아, 카운트다운 하는 프로그램을 만들어 봅시다.
# a = int(input())
# for i in range(a+1):
#   print(a)
#   a -= 1
#   if a == 0:
#     break

# # todo 3 : n!을 반복문을 통해 구현하세요. n!란, 1부터 n까지의 곱을 의미합니다.
# n = int(input())
# n_pack = 1

# for i in range(1, n+1):
#   n_pack *= i

# print(n_pack)

# #실습 1
# list_d = [[1 if(i+j) % 2 == 1
#            else 0
#            for i in range(5)]
#           for j in range(5)]

# for rows in list_d:
#   print(rows)

# #실습 2
# list_d = [[1 if (i ==0 or j == 4 or i == 4 or j == 0) else 0 for i in range(5)] for j in range(5)]
# # i ==0 or j == 4 or i == 4 or j == 0
# for rows in list_d:
#   print(rows)

# #실습 3(시험에 x자 형태로 출력하는게 나옴)
# list_d = [[1 if i == j else 0 for i in range(5)] for j in range(5)]

# for rows in list_d:
#   print(rows)

# #실습 4
# list_d = [[1 if i >= j
#            else 0
#            for i in range(5)]
#           for j in range(5)]

# for rows in list_d:
#   print(rows)

# #실습 5
# list_d = [[i * 4 + j for j in range(4)] for i in range(4)]

# for rows in list_d:
#   print(rows)

# #미로
# maze = [
#     ['S', '0', '1', '0', '0'],
#     ['1', '0', '1', '1', '0'],
#     ['0', '0', '0', '0', '0'],
#     ['0', '1', '1', '1', '1'],
#     ['0', '0', '0', '0', 'E']
# ]

# stack = [[0,0]]
# found = False


# while len(stack) > 0 :
#   curr = stack.pop()
#   r = curr[0]
#   c = curr[1]

#   if maze[r][c] == 'E':
#     found = True
#     break

#   maze[r][c] ='2'

#   directions =[[-1,0], [1,0], [0,-1], [0,1],[-1,-1], [1,-1], [1,1], [-1,1]]

#   for dr in directions:
#     nr = r + dr[0]
#     nc = c + dr[1]
#     if 0 <= nr < 5 and 0 <= nc < 5 :
#       if maze[nr][nc] == '0' or maze[nr][nc] == 'E' :
#         stack.append([nr, nc])

# if found == True:
#   print("경로 탐색 완료")
# else :
#   print("경로 탐색 실패")

# for row in maze:
#     print(row)

# a = str(input())
# for i in a:
#     if i.islower():
#         print(i.upper(), end ='')
#     elif i.isupper():
#         print(i.lower(), end='')

# names = ["Alice", "Bob", "Charlie"]

# names_dict = {name : len(name)   for name in names}

# print(names_dict)

# name = ['merona', 'gugucon']
# price = [500, 1000]

# name_dict = {k : v * 2 for k,v in zip(name, price)}
# print(name_dict)

# name = ['merona', 'bibibic', 'shark bar']
# price = [300, 400, 250]
# jaego = [20, 3 , 100]

# ice_bar = {'merona':{'price' : 300, 'jaego' : 20 }, 'bibibic' :{'price' : 400, 'jaego' : 3 }, 'shark bar':{'price': 250, 'jaego':100}}
# print(ice_bar['merona']['price'])

# ice_bar = {'world_con':{'price' : 500,'jaego':7}}

# ice_bar2 = {'merona' : {'price' : 300, 'jaego' : 20}, 'bibibic' : {'price' : 400, 'jaego' : 3 }}

# ice_bar.update(ice_bar2)

# print(ice_bar['merona']['price'])


# icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# new_product = {'팥빙수':2700, '아맛나':1000}

# icecream.update(new_product)

# print(icecream)

# raw_data = [
#     ["Park", 85, 90, 78],
#     ["Kim", 92, 88, 95],
#     ["Lee", 78, 85, 88]
# ]

# data_dict = {data[0] : data[1:]  for data in raw_data}

# print(data_dict)

# books_raw = [
#     ["파이썬 정복", "김철수", True],
#     ["데이터 분석", "이영희", False],
#     ["알고리즘 입문", "박민수", True]
# ]

# books_dict = {book[0] : {'저자' : book[1], '대여가능여부':book[2]} for book in books_raw}

# print(books_dict)

# scores = {"철수": 75, "영희": 90, "민수": 85, "지수": 60}

# sc_dict = {name : score for name, score in scores.items() if score >= 80}

# print(sc_dict)

# teams = {
#     "A팀": {"철수": 10, "영희": 20, "민세" : 50},
#     "B팀": {"민수": 15, "지수": 25, "영수" : 50}
# }

# team = input()
# print(sum(teams[team].values()))

# movies = {
#     "인셉션": [4, 5, 5],
#     "아바타": [3, 4]
# }

# mv = input()

# sc = int(input())

# if mv in movies:
#   movies[mv].append(sc)
# else:
#   movies[mv] = [sc]

# avg = sum(movies[mv]) / len(movies[mv])
# print("평점 평균", avg)

# import threading
# import time

# shared_counter = 0

# def increase():
#     global shared_counter
#     for _ in range(1000):

#         curr = shared_counter
#         time.sleep(0.000001)
#         shared_counter = curr + 1

# def decrease():
#     global shared_counter
#     for _ in range(1000):

#         curr = shared_counter
#         time.sleep(0.000001)
#         shared_counter = curr - 1

# thread1 = threading.Thread(target=increase)
# thread2 = threading.Thread(target=decrease)

# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()

# print(shared_counter)

# stack = []

# txt = input()

# for i in range(len(txt)):
#   if txt[i] != '+' and txt[i] != '-' and txt[i] != '*' and txt[i] != '/':
#     stack.append(int(txt[i]))
#   else:
#     op1 = stack.pop()
#     op2 = stack.pop()
#     if txt[i] == '+':
#       stack.apppend(op2 + op1)
#     elif txt[i] == '-':
#       stack.append(op2 - op1)
#     elif txt[i] == '*':
#       stack.append(op2 * op1)
#     elif txt[i] == '/':
#       stack.append(op2 / op1)
# print(stack.pop())

# a,b,c = map(int,input().split( ))

# sum = a + b + c
# avg = sum / 3
# print(f"중간고사 평균 점수 : {avg}")

# # def add_ten(a):
# #   return a + 10
# # print(add_ten(10))

# # y = lambda x : x + 10
# # print(y(10))

# products = [
#     {"name": "감자", "price": 500},
#     {"name": "고구마", "price": 1200},
#     {"name": "양파", "price": 800}
# ]

# new_pro = sorted(products, key = lambda x : x ["price"])
# print(new_pro)

# languages = ["python", "JavaScript", "C++", "react"]

# new_lang = sorted(languages, key = lambda x : -len(x))

# print(new_lang)

# students = [("김철수", 80), ("이영희", 95), ("박민수박", 80)]

# new_stu = sorted(students, key = lambda x : (-x[1], len(x[0])))

# print(new_stu)

# words = ["apple", "bat", "code", "atom", "car"]

# new_words = sorted(words, key = lambda x : (len(x), x[0]))

# print(new_words)

# dates = ["2024-03-01", "2023-12-25", "2024-01-01", "2023-05-05"]

# new_date = sorted(dates, key = lambda x : (x.split('-')[1], x.split('-')[2]))

# print(new_date)

# scores = [("A", 80, 90), ("B", 95, 70), ("C", 85, 85)]

# new_score = sorted(scores, key = lambda x :(-(x[1] + x[2]), x[0]))

# print(new_score)

# posts = [
#     {"type": "free", "title": "안녕", "id": 1},
#     {"type": "notice", "title": "필독", "id": 2},
#     {"type": "free", "title": "질문", "id": 3}
# ]

# new_post = sorted(posts, key = lambda x : (-(x["type"]=='notice'), -x['id']))

# print(new_post)

# stores = [("호식이 두마리 치킨", 3, 4), ("도미노피자", -1, 2), ("버거킹", 5, 0), ("삼첩분식", 1, 1)]

# new_store = sorted(stores, key = lambda x : ((x[1] ** 2 + x[2] ** 2), len(x[0])))

# print(new_store)

# kt = {'지훈', '강현', '민세', '한성'}
# lotte = {'강현', '민세', '은체', '도윤'}
# hanwa = {'지훈', '한성', '지희', '민세'}

# print((kt & hanwa) - lotte)

# dice1 = (1, 2, 3, 4, 5, 6)
# dice2 = (2, 3, 5, 7, 11, 13)

# sums = []

# for i in dice1:
#   for j in dice2:
#     sums.append(i+j)
# print(set(sums))

# dice1 = (1, 2, 3, 4, 5, 6)
# dice2 = (2, 3, 5, 7, 11, 13)

# sum_set = {i+j for i in dice1 for j in dice2}
# print(sum_set)

# # 필수 역량
# required_skills = {"Python", "Git"}

# # 지원자별 기술 스택 데이터
# applicants = {
#     "지훈": {"Python", "Java"},
#     "강현": {"Python", "Git", "C++"},
#     "민세": {"JavaScript", "Git"},
#     "한성": {"Python", "Linux"}
# }
# Yaho = []
# for i in applicants.keys():
#   if required_skills == applicants[i] & required_skills:
#     Yaho.append(i)
# print(Yaho)

# # 필수 역량
# required_skills = {"Python", "Git"}

# # 지원자별 기술 스택 데이터
# applicants = {
#     "지훈": {"Python", "Java"},
#     "강현": {"Python", "Git", "C++"},
#     "민세": {"JavaScript", "Git"},
#     "한성": {"Python", "Linux"}
# }

# # 부분 집합을 이용한 풀이
# yaho = [k for k, v in applicants.items() if v > required_skills]

# print(yaho)

# list_a = ["Alice@test.com", "bob@test.com", "ALICE@test.com", "charlie@test.com"]
# list_b = ["alice@test.com", "BOB@test.com", "david@test.com"]

# new_a = set([i.lower() for i in list_a])
# new_b = set([i.lower() for i in list_b])

# print(len(new_a & new_b))

# ms_ma = 99
# ms_sc = 87.8
# ms_sa = 69.1
# ms_ds = 40

# ms_score = [99, 87.8, 69.1, 40]

# ms_score = {
#     '국어':99,

# }

# class Student:
#   def __init__(self, name, math, money):
#     self.name = name
#     self.math = math
#     self.__money = money

#   def print_score(self):
#     print(f"이름 : {self.name} , ", end = ' ')
#     print(f"수학 성적 : {self.math} , ", end = ' ')
#     print(f"전 재산 : {self.__money}")

# s1 = Student('민세', 99, 100000)
# s2 = Student('태인', 90, 5000)
# s3 = Student('승곤', 90, 350000)
# s4 = Student('세영', 99, 34000)

# stu = [s1, s2, s3, s4]

# for i in stu:
#   i.print_score()

# def fac(n):
#   if n == 1 : return 1

#   return n * fac(n-1)

# print(fac(5))

# def asterisk(n):
#   if n >= 1:
#     asterisk(n // 2)
#     asterisk(n // 2)

#   print("*", end="")

# asterisk(5)

# # 1. 피보나치 수열의 n번째 항을 구하는 재귀함수를 작성하세요.

# # 피보나치 수열 : 1, 1, 2, 3, 5, 8, 13.... 과 같이 이전 항의 합으로 구성



# # 2. a의 n 제곱을 구하는 함수를 재귀함수로 작성하세요.

# def nx(a, n):
#   if a == 1:
#     return 1

#   elif n == 1:
#     return a

#   return a * nx(a, n-1)

# print(nx(2, 3))

# # 3. 1 + 1/2 + 1/3 + ..... + 1/n을 구하는 함수를 재귀함수로 작성하세요.

# def ss(n):
#   if n == 1 or n == 0:
#     return 1
#   else :
#     return 1/n + ss(n-1)

# print(ss(4))

# # 4. for문과 sum을 사용하지 않고, 리스트의 합을 구하는 재귀함수를 작성하세요.


# # 5. 문자열을 뒤집는 함수를 재귀함수로 작성하세요.

# class Student:

#   c_name = "1학년 3반"
#   #공유되는 값(클래스 변수), 객체끼리 공유하는 것

#   def __init__(self, name, pos):
#     self.name = name
#     self.pos = pos

# stu1 = Student("권민세", "반장")
# #객체끼리의 값은 독립되어 있다(인스턴스 변수), 생성자 안에 있는 변수
# stu2 = Student("박태인", "미남")


# Student.c_name = "2학년 1반"

# print(stu1.name, stu1.pos, Student.c_name)

# print(stu2.name, stu2.pos, Student.c_name)

# class Account:
#   interest_rate = 0.02

#   def __init__(self, owner, balance):
#     self.owner = owner
#     self.balance = balance

#   def deposit(self, amount):
#     self.balance += amount

#   def apply_interest(self):
#     self.balance += (self.balance) * Account.interest_rate

# # 학테스트 코드
# acc = Account("권민세", 10000)
# acc.deposit(5000)
# acc.apply_interest()
# print(f"{acc.owner}님의 최종 잔액: {acc.balance}원")
# # 출력 결과 예시: 홍길동님의 최종 잔액: 15300.0원

# class Product:

#   free_shipping_limit = 30000

#   def __init__(self, name, price):
#     self.name = name
#     self.price = price

#   def get_shipping_fee(self):
#     if self.price >= Product.free_shipping_limit:
#       return ("무료 배송 대상입니다.")
#     elif self.price < Product.free_shipping_limit:
#       return ("배송비 3,000원이 부과 됩니다")

# p1 = Product("무선 마우스", 25000)
# p2 = Product("기계식 키보드", 45000)

# print(f"{p1.name}: {p1.get_shipping_fee()}") # 배송비 부과 안내 출력
# print(f"{p2.name}: {p2.get_shipping_fee()}") # 무료 배송 안내 출력

# class Bssm_one :
#   def __init__(self, name, score):
#     self.name = name
#     self.score = score

#   def get_score(self):
#     print(f'{self.name}의 평균은 {sum(self.score) / len(self.score)}')

# class OneThree(Bssm_one) :

#   def __init__(self, name, score, height):
#     super().__init__(name, score)
#     self.height = height
  
#   def get_score(self):
#     super().get_score()
#     print('수고했다')
#     print(f'키는 : {self.height}')

# class OneFour(Bssm_one) :

#   def get_score(self):
#     super().get_score()
#     print('얻드려라')

  
# s1 = OneThree('민세', [80, 30, 100], 180)

# s1.get_score()

# s2 = OneFour('한성',[70, 70, 70])

# s2.get_score()


# class Animal:
#   def __init__(self, name):
#     self.name = name

#   def make_sound(self):
#     print("동물이 소리를 냅니다")

# class Dog(Animal):
  
#   def make_sound(self):
#     super().make_sound()
#     print(f"{self.name}가 멍멍! 짖습니다.")


# class Cat(Animal):
#   def make_sound(self):
#     super().make_sound()
#     print(f"{self.name}가 야옹~ 하며 웁니다.")

# # 테스트 코드
# dog = Dog("개죽이")
# cat = Cat("나비")

# dog.make_sound()
# cat.make_sound()

# print(dog.name)

# class Beverage:

#   def __init__(self, name, price):
#     self.name = name
#     self.price = price

#   def get_info(self):
#     return f"{self.name} - {self.price}원"

# class Coffee(Beverage):
#   def __init__(self, name, price, temperature='Hot'):
#     super().__init__(name, price)
#     self.temperature = temperature

#   def get_info(self):
#     final_price = self.price
#     if self.temperature == "Ice":
#       final_price += 500

#     return f"[{self.temperature}] {self.name} - {final_price}원"

# class BubbleTea(Beverage):
#   def __init__(self, name, price, has_pearl = False):
#     super().__init__(name, price)
#     self.has_pearl = has_pearl

#   def get_info(self):
#     final_price = self.price
#     if self.has_pearl:
#       return f"{self.name} (펄 추가) - {final_price}원"
#     else:
#       return f"{self.name} - {final_price}원"

# c = Coffee("아메리카노", 4000, "Ice")
# print(c.get_info())

# b = BubbleTea("타로 버블티", 5000, True)
# print(b.get_info())

# class FishBread:
#   total = 0

#   def __init__(self, name, price):
#     self.name = name
#     self.price = price
#     FishBread.total += 1

#   @classmethod
#   def mak_pat_bread(cls): #cls는 self랑 비슷함
#     print('팥붕 만들기') 
#     return cls('팥붕', 600)


#   @classmethod
#   def mak_sue_bread(cls): #cls는 self랑 비슷함
#     print('슈붕 만들기') 
#     return cls('슈붕', 1000)

#   @staticmethod
#   def cal_bags(count):
#     print(f'빵{count}개에 필요한 봉투 갯수 : {count//5}')

# b1 = FishBread.mak_pat_bread()

# b2 = FishBread.mak_pat_bread()

# b3 = FishBread.mak_pat_bread()

# b4 = FishBread.mak_sue_bread()

# FishBread.cal_bags(10)

# class Student:
#   total_students = 0

#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     Student.total_students += 1
  
#   @classmethod
#   def register_freshman(cls,name):
#     return cls(name, 8)

#   @staticmethod
#   def is_adult(age):
#     if age >= 20 :
#       return True
#     else :
#       return False

# class Pizza:
#   total_sales = 0

#   def __init__(self, name, price):
#     self.name = name
#     self.price = price

#   @classmethod
#   def order_cheese_pizza(cls):
#     Pizza.total_sales += 15000
#     return cls("Cheese Pizza", 15000)
    
#   @staticmethod
#   def calculate_delivery_fee(distance):
#     if distance >= 3:
#       return 5000
#     else :
#       return 3000

# class linkedlist:
#   def __init__(self):
#     self.head = None
#     self.size = 0

#   def isEmpty(self):
#     return self.head is None

#   def create_node(self, data, link = None):
#     return {'data':data, 'next':link}

#   def display(self):
#     current_node = self.head
#     while current_node:
#       print(current_node['data'], end= '->')
#       current_node = current_node['next']
#     print("None")

#   def insert(self, data, target = None):
#     new_node = self.create_node(data)
#     if self.isEmpty():
#       self.head = new_node
#       self.size += 1
#       return
#     if target == None:
#       new_node['next'] = self.head
#       self.head = new_node
#       self.size += 1
#       return
#     current_node = self.head
#     while current_node:
#       if current_node['data'] == target:
#         new_node['next'] = current_node['next']
#         current_node['next'] = new_node
#         self.size += 1
#         return
#       current_node = current_node['next']
#     print(f"Target '{target}' not found in the list")

#   def delete(self, target):
#     if self.isEmpty():
#       print('Empty')
#       return
#     prev_node = None
#     current_node = self.head
#     while current_node:
#       if current_node['data'] == target:
#         if prev_node == None:
#           self.head = self.head['next']
#         else:
#           prev_node['next'] = current_node['next']
#           self.size -= 1
#           return
#       prev_node, current_node = current_node, current_node['next']
#     print(f"Target '{target}' not found in the list")

#   def append(self, data):



# ll = linkedlist()
# ll.insert('a')
# ll.insert('c')
# ll.display()
# ll.insert('b','c')
# ll.display()
# ll.delete('b')
# ll.display()
# ll.delete('c')
# ll.display()
# ll.delete('a')
# ll.display()
# ll.append('x')
# ll.append('z')
# ll.insert('y', 'x')
# ll.display()