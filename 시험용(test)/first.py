#1번 문제 (기초 - 조건문과 반복문)✅
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #-> 숫자 저장 리스트
result = 0

for num in numbers: # => num은 numbers 리스트에 들어있는 숫자 값을 가리킴
    if num % 2 == 0: # -> numbers 리스트에서 들고온 값 num이 짝수일경우
        result += num # -> result 변수에 저장한다
print(result) #-> 저장한 결과 출력

#2번 문제 (기초 - 문자열 다루기) ✅
text = "Python"
reversed_text = "" #=> 빈 문자열

for char in text: #=> Python에서 한글자씩 가져온다
    reversed_text = char + reversed_text # -> 빈 문자열에 한글자씩 넣는데, 새로운 문자 + 기존의 문자를 넣기에 반대로 들어가진다.

print(reversed_text)

#3번 문제 (중급 - 리스트와 인덱스) ❌
data = [10, 20, 30, 40, 50]
new_data = []

for i in range(len(data) - 1, -1, -1): # -> 4부터 -1까지 반복을 돌때마다 -1을 한다.(틀린 설명)
    # -> 원래 range(a, b)를 하게 되면 b 전까지 반복을 돌리기 때문에 4~0이 된다.
    new_data.append(data[i]) #-> data[4]는 50이고, data[-1]도 50 이기에 new_data에는 50의 값만 들어간다.(틀린 설명)
    # -> 4 ~ 0까지의 값이 new_data에 들어가므로 50, 40, 30, 20, 10의 값이 원래 data 순서의 반대로 저장된다.
print(new_data)

#4번 문제 (중급 - 함수와 재귀)✅
def func(n):
    if n <= 1: # -> n이 1보다 작거나 같을경우 1을 반환한다
        return 1
    return n + func(n - 1) # -> 아니라면 n 더하기 func(n-1) 을 하여서 값을 반환한다.

print(func(4)) # -> 4 + 3 + 2 + 1 => 10이다

#5번 문제 (응용 - 딕셔너리 활용)✅
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = {}

for word in words: # -> 문자열을 저장한 리스트에서 하나씩 꺼내온다
    if word in count: # -> 만약 이미 카운트 안에 있다면 word를 키로 하는 값을 1 증가
        count[word] += 1
    else:
        count[word] = 1 # -> 없다면 1로 설정

print(count) # -> 전체 count 출력

#6번 문제 (기초 - 리스트 슬라이싱)✅
text = "Programming"
sub_text = text[2:7:2] #-> 2부터 6까지 2칸씩 뛰어넘긴 값을 저장

print(sub_text) # -> orm

#7번 문제(중급 - 조건문과 흐름 제어)✅
numbers = [10, 15, 20, 25, 30]
result = []

for num in numbers:
    if num % 2 == 0: # num의 값이 짝수라면 다음 반복으로 넘어간다
        continue
    if num > 20: # num의 값이 20보다 크다면 반복 중단
        break
    result.append(num) # -> 15가 저장

print(result) # -> 15 출력

#8번 문제(중급 - 2차원 리스트 다루기)❌
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
total = 0

for i in range(len(matrix)): # => 3번 반복
    total += matrix[i][i] # -> 1, 4, 7 저장(틀린 설명)
    # -> total이라는 변수에 1, 4, 7의 값을 더하여 저장한다.

print(total) # -> 1, 4, 7 출력(틀린 설명)
#-> 1, 4, 7의 합인 12가 출력된다.

#9번 문제 (응용 - 리스트 컴프리헨션)✅
words = ["cat", "dog", "elephant", "bat"]
filtered_words = [w.upper() for w in words if len(w) <= 3] 
# -> words에서 꺼내온 값 w가 길이가 3보다 작거나 같을때 문자열을 대문자로 바꾸어 리스트에 저장

print(filtered_words) # CAT, DOG, BAT 출력

#10번 문제 (응용 - 전역/지역 변수 Scope)✅
x = 10

def update_val(): # -> 함수가 실행되면 x = 20, 그러한 x의 값을 반환한다.
    x = 20
    return x

update_val()
print(x)
# -> 10이 출력된다. 함수를 실행시켜도 전역 변수가 아닌 함수안의 지역변수 x의 값을 20으로 바꾸고 반환했기 떄문이다.

#11번 문제 (기초 - 문자열 메서드와 조건)✅
text = "hello_world_python"
parts = text.split("_") # -> _로 문자열을 구분하여 parts에 저장
result = ""

for p in parts: # -> 리스트 형태의 parts에서 뽑아온 값 p
    result += p.capitalize() # 그 값 p를 앞에 한자리만 대문자로 변경하여 저장한다

print(result) # => Hello, World, Python
#피드백: 쉼표(,) 없이 빈 문자열 result에 연속으로 붙어 출력됩니다.

#12번 문제 (중급 - 2차원 리스트 누적)✅
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_sums = []

for row in matrix: # -> row는 matrix안에 있는 큰 리스트들을 가리킴
    s = 0
    for val in row: # -> value는 matrix안에 있는 리스트들의 하나의 값들을 가리킴
        s += val # -> s에 1, 2, 3 등등 하나의 리스트 값들을 다 더한다
    row_sums.append(s) # -> row_sums에 합을 저장한다.

print(row_sums) # -> 6, 15, 24

#13번 문제 (중급 - 집합 Set 활용)✅
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

set_a = set(a) # -> 리스트 형태의 a를 집합의 형태로 바꾼다
set_b = set(b) # -> 리스트 형태의 b를 집합의 형태로 바꾼다

result = list(set_a - set_b) # -> a에서 b에 있는 값들을 빼고 리스트 형태로 바꾼다.
result.sort() # -> 집합에는 순서가 없기에 집합에서 리스트로 바뀐값들을 sort로 정렬해준다.

print(result) # => 1, 2

#14번 문제 (응용 - 삼항 연산자 포함 컴프리헨션)✅
numbers = [1, 2, 3, 4, 5]
result = [x * 2 if x % 2 == 0 else x for x in numbers]
# -> x가 짝수 이면 2를 곱하여 result에 저장하고, 아니라면 원본 값을 저장한다.

print(result) # => 1, 4, 3, 8, 5

#15번 문제 (응용 - 가변 인자 *args)✅
def calc_sum(*args): # -> 리스트 전체값이 들어온다.
    total = 0
    for num in args:
        if num < 0: # num의 값이 0보다 작다면 해당 반복은 건너뛴다
            continue
        total += num # num의 값이 0보다 크다면 total에 더한다.
    return total # 반복이 끝난후 total의 값을 리턴한다.

print(calc_sum(10, -5, 20, -3, 30)) # => 60

#16번 문제 (심화 - zip과 enumerate 혼합)✅
keys = ["a", "b", "c"]
values = [10, 20, 30]

result = {}
for idx, (k, v) in enumerate(zip(keys, values)): # -> idx는 반복 횟수, k는 키, v는 벨류
    if idx % 2 == 0: # -> 반복 횟수가 짝수일때
        result[k] = v * 2 # -> result 딕셔너리에 키가 k, 벨류가 v에 2를 곱한 값을 넣는다.

print(result) # -> a  20, c  60

#17번 문제 (심화 - 람다와 sort Key 지정)✅
students = [
    ("Kim", 85),
    ("Lee", 92),
    ("Park", 85),
    ("Choi", 78)
]

students.sort(key=lambda x: (-x[1], x[0]))#-> 점수 내림차순, 점수가 같다면 이름 오름차순 정렬

print(students[0][0]) # -> Lee

#18번 문제 (심화 - 문자열 회구(Palindrome)와 슬라이싱)❌
text = "A man, a plan, a canal: Panama"
cleaned = [char.lower() for char in text if char.isalnum()]
# -> text에서 가져온값 char에 알파벳과 숫자말고 다른것으로 되있다면 소문자로 바꾸어 cleand에 저장한다(틀린 설명)
# => char.isalnum()은 알파벳과 숫자일 때 True가 됩니다. 따라서 특수문자/공백을 제외한 순수 글자만 소문자로 모아서 저장합니다.

is_palindrome = cleaned == cleaned[::-1]
#만약 cleand의 원본과 cleand를 뒤집은 것이 같다면 True, 아니라면 False를 is_palindrome에 저장(틀린 설명)
#백과 특수문자를 제거하면 "amanaplanacanalpanama"가 됩니다. 이 문장은 앞에서 읽으나 뒤에서 읽으나 똑같은 회문(Palindrome)이므로 True가 출력됩니다!

print(is_palindrome)# -> False

#19번 problem (심화 - 투 포인터 기본 알고리즘)❌
nums = [1, 3, 5, 7, 9]
target = 8

left, right = 0, len(nums) - 1
count = 0

while left < right: # -> left가 right보다 작을동안 반복
    current_sum = nums[left] + nums[right]# nums[0] + nums[0] 부터 시작
    if current_sum == target: # -> 만약 타켓과 같은 값이라면 count 1 증가, left 1 증가, right 1 감소
        count += 1
        left += 1
        right -= 1
    elif current_sum < target: # left와 right의 합이 target보다 작을때 left에 1증가
        left += 1
    else: # 아니라면 1 감소
        right -= 1

print(count) # -> 답을 못구하겠음

"""
작성하신 해석 중 오류: nums[0] + nums[0]부터 시작이 아니라, left = 0, right = 4이므로 nums[0] + nums[4] (1 + 9 = 10)부터 시작합니다.
실제 출력값: 2
단계별 흐름 (target = 8):
left=0(값:1), right=4(값:9) → 합: 10>8 → right 1 감소
left=0(값:1), right=3(값:7) → 합: 8==8 → count 1 증가, left 1 증가, right 1 감소
left=1(값:3), right=2(값:5) → 합: 8==8 → count 1 증가, left 1 증가, right 1 감소
left=2, right=1 → left < right 조건 종료!
따라서 1+7=8, 3+5=8 두 쌍이 찾아져서 2가 출력됩니다.
"""

#20번 문제 (심화 - 딕셔너리와 get() 메서드 응용)✅
data = ["apple", "banana", "apple", "cherry"]
inventory = {}

for item in data:
    inventory[item] = inventory.get(item, 0) + 1
    # -> inventory에 item을 키로 넣고, inventory에 item 키가 없을 경우 0을 반환 이때 +1을 하여 저장
    # apple : 2, banana : 1, cherry : 1
total_items = sum(inventory.values()) # -> inventory에 있는 키의 값들을 반환후 sum 함수로 합쳐서 total_items에 저장
print(total_items) # -> 4