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