# 알고리즘

#### “문제를 해결하기 위해 입력을 받아 원하는 결과를 출력하도록  만든 유한한 절차 또는 방법”

## 개념과 조건

- 알고리즘의 조건(특성)
    - 입력 : 0개 이상의 입력을 가져야 한다
    - 출력 : 최소 1개 이상의 결과를 만들어야 한다
    - 명확성 : 각 단계가 명확해야한다
    - 유한성 : 유한한 시간과 단계를 거쳐 실행이 완료되고 종료되어야 한다
    - 수행 가능성 : 모든 명령이 수행 가능해야 한다

## 자료구조와 알고리즘

- 자료구조
    - 자료를 효율적으로 저장, 관리하는 방법
    - 자료구조 + 알고리즘 = 빠른 프로그램

| 자료구조 | 언제 쓰는가? |
| --- | --- |
| 배열 | 빠르게 접근 |
| 연결리스트 | 삽입,삭제 많음 |
| 스택 | 최근 작업 |
| 큐 | 순서대로 처리 |
| 트리 | 계층 표현 |
| 그래프 | 여러 대상 사이의 연결 관계와 이동경로를 표현할때 |
- 스택
    - push() : 스택에 비어있는 맨 위의 칸에 데이터 삽입
    - pop() : 스택의 맨 위칸의 데이터를 삭제 후 반환
    - isFull() : 스택의 높이가 ‘스택의 크기 - 1’ 일때 삽입하면 오버플로우 오류 반환
    - isEmpty() : 스택의 아무 데이터가 없을때 삭제를 수행하면 언더플로우 오류 반환
    - peek() : 스택의 가장 위에 있는 요소에 있는 값을 제거하지 않고 반환
- 큐
    - enqueue() : rear를 +1 시킨후 맨뒤에 데이터 저장
    - dequeue() : front를 +1 시킨후 증가 시킨 위치의 데이터 삭제
    - isFull() : rear의 크기가 ‘큐의 크기 -1’ 일때 삽입하면 오버플로우 오류 발생
    - isEmpty() : rear == front일때 삭제 수행하면 언더플로우 오류 발생
- 연결리스트
    - insert() : 새로운 노드를 만들고 연결을 변경하여 원래 위치에 삽입
    - delete() : 삭제할 노드를 제거하고 앞 뒤 노드의 연결을 변경
    - search() : 노드를 순서대로 따라가며 원하는 데이터를 찾는다.
    - traverse() : 처음부터 링크를 따라가며 전체 노드 방문

# Big - O, 순차 탐색

### “좋은 알고리즘은 정답을 구할 뿐 아니라 시간과 메모리도 적절하게 사용해야한다.”

## Big - O

- Big - o
    - 입력이 커질수록 실행 횟수, 메모리가 어떻게 증가하는가?

| 구분 | 의미 |
| --- | --- |
| 시간 복잡도 | 입력 크기에 따라 실행량이 얼마나 증가하는가? |
| 공간 복잡도 | 입력 크기에 따라 추가 메모리가 얼마나 필요한가? |
- 공간 복잡도
    - 입력 크기 n이 증가할 때 알고리즘이 추가로 사용하는 메모리의 양이 어떻게 증가하는지를 나타내는것
- 시간 복잡도
    - 문제를 해결하는데 소요되는 시간을 측정하는 방법

| Big - O | 증가 형태 | 의미 | 대표적인 예 |
| --- | --- | --- | --- |
| O(1) | 일정 | 입력 크기 n이 증가해도 필요한 연산량이 일정함 |   • 배열의 특정 인덱스 접근 |
| O(log n) | 로그형태로 증가 | 입력 크기가 증가해도 연산량은 매우 천천히 증가함 |   • 이진 탐색 |
| O(n) | 선형적으로 증가 | 입력 크기 n에 비례하여 연산량이 증가함 |   • 순차 탐색 |
| O(n log n) | n log n 형태로 증가 | O(n) 보다 빠르게, O(n^2)보다 느리게 증가함 |   • 합병 정렬, 평균적인 퀵정렬 |
| O(n^2) | 제곱 형태로 증가 | 입력 크기의 제곱에 비례하여 연상량이 증가함 |   • 선택정렬, 버블 정렬, 삽입 정렬의 평균/최악 |
| O(n^3) | 세 제곱 형태로 증가 | 입력 크기의 세제곱에 비례하여 연상량이 증가함 |   • 3중 반복문 |
| O(2^n) | 지수 형태로 증가 | n이 증가할수록 연산량이 매우 그격하게 증가함 |   • 모든 부분 집합 탐색 |
| O(n!) | 팩토리얼 형태로 증가 | 가능한 모든 순서를 고려하여 연산량이 극도로 빠르게 증가함 |   • 모든 순열 탐색 |
- 연산 증가 속도
    - O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)
    - → 갈수록 느려지는거

## 순차 탐색

- 순차 탐색
    - 배열의 앞에서 부터 차례로 찾는 탐색
- 자연어
    - 우리가 사용하는 언어로 표현하는 방법
    - 예시
        
        ```smalltalk
        1. 첫번째 원소부터 확인
        2. 같으면 종료
        3. 아니면 다음 원소 확인
        4. 끝까지 없으면 실패
        ```
        
- 순서도
    - 일의 순서와 정보의 흐름을 쉽게 파악할 수 있도록 약속된 기호를 사용하여 도표로 표시하는 방법
    - 도형 및 기호
        
        !도형 및 기허.jpeg
        
    - 예시
        
        !순서도.jpeg
        
- 의사 코드
    - 특정 프로그래밍 언어의 문법적 제약을 받지 않지만 프로그래밍 언어의 문법과 비슷하게 기술하는 방법
    - 예시
        
        ```smalltalk
        FOR 모든 원소
        	IF 찾았다
        		RETURN 위치
        RETURN -1
        ```
        
- 프로그래밍 언어
    - 컴퓨터에서 실행 가능한 프로그래밍 언어로 기술하는 법
    - 예시
        
        ```c
        #include <stdio.h>
        int linearSearch(int arr[], int size, int target){
            int bigo = 0;
            for(int i = 0; i < size; i++){
                if(arr[i] == target){
                    bigo += 1;
                    return bigo;
                }
                else{
                    bigo += 1;
                }
            }
            return size;
        }
        int main(void){
            int arr[] = {13, 8, 27, 4, 19};
            int size = sizeof(arr) / sizeof(arr[0]);
            int target;
        
            printf("찾을 숫자 입력: ");
            scanf("%d", &target);
        
            int result = linearSearch(arr, size, target);
        
            if(result == -1){
                printf("비교 횟수 : %d\n", result);
                printf("%d는 배열에 없습니다\n", target);
            }
            else{
                printf("비교 횟수 : %d\n", result);
                printf("%d은 %d번째 인덱스에서 찾았습니다.", target, result-1);
            }
            return 0;
        }
        ```
        

## 연결 리스트

- 연결 리스트
    - 여러 데이터를 노드 단위로 저장하고, 각 노드가 다음 노드의 위치를 가리키도록 연결한 자료구조이다.
- 배열과 연결 리스트의 차이
    - 배열은 인덱스를 통해 원하는 위치의 데이터에 접근 가능하고
    - 연결 리스트는 인덱스가 없으므로 첫 번째 노드부터 next를 따라 이동한다.
- 노드
    - 연결 리스트를 구성하는 하나의 데이터 단위
    - 구성
        - data - 실제 저장할 데이터
        - next - 다음 노드의 주소
        - head - 연결리스트의 첫 번째 노드를 가리키는 포인터
    - 활용 문제
        
        ```c
        #include <stdio.h>
        #include <stdlib.h>
        
        typedef struct Node{
            int data;
            struct Node* next;
        }Node;
        
        void insertBack(Node** head, int data){
            Node * newNode = malloc(sizeof(Node));
        
            newNode -> data = data;
            newNode -> next = NULL;
        
            if(*head == NULL){
                *head = newNode;
                return;
            }
        
            Node* current = *head;
        
            while(current -> next != NULL){
                current = current -> next;
            }
            current -> next = newNode;
        }
        
        Node* linnearSearch(Node* head, int target){
            Node* current = head;
            while(current != NULL){
                if(current -> data == target){
                    return current;
                }
                current = current -> next;
            }
            return NULL;
        }
        
        int main(void){
            Node* head = NULL;
        
            insertBack(&head, 17);
            insertBack(&head, 8);
            insertBack(&head, 25);
            insertBack(&head, 31);
            insertBack(&head, 12);
            insertBack(&head, 40);
            insertBack(&head, 6);
        
            int target;
        
            printf("찾을 숫자 입력: ");
            scanf("%d", &target);
        
            Node* result = linnearSearch(head, target);
            if(result != NULL){
                printf("%d를 찾았습니다\n", target);
            }
            else{
                printf("%d를 찾지 못했습니다.\n", target);
            }
        
            Node* current = head;
        
            while(current != NULL){
                Node* temp = current;
                current = current -> next;
                free(temp);
            }
        }
        ```
        

# 포인터와 구조체

## 포인터

- 포인터 변수
    
    ```c
    int a = 10;
    int* p = &a;
    ```
    
    - 주소를 지정하는 변수
    - *p : p가 가지고 있는 주소를 가리키는 대상에 접근한다 → 역참조

```c
int a = 25;
int *p = &a;
(&a = 150, &p = 300)
```

| 표현 | 의미 | 값 |
| --- | --- | --- |
| a | a에 저장된 값 | 25 |
| &a | a의 주소 | 150 |
| p | p에 저장된 주소 | 150 |
| &p | p 자신의 주소 | 300 |
| *p | p가 가리키는 주소의 값 | 25 |
- *의 역할
    - int *p
        - p는 int를 가리킬수있는 포인터 변수(선언)
    - *p = 30
        - p가 가리키는 대상에 접근 → 사용할때
- 이중 포인터
    - 포인터 변수의 주소를 저장하는 포인터
    
    ```c
    int a = 10;
    int *p = &a;
    int **pp = &p;
    
    pp -> p -> a
    ```
    
    | 표현 | 의미 |
    | --- | --- |
    | a | a의 값 |
    | &a | a의 주소 |
    | p | p가 가리키는 값의 주소 |
    | *p | p가 가리키는 값의 원본(a = 10) |
    | &p | p의 주소 |
    | pp | pp가 가리키는 값의 주소 |
    | *pp | pp가 가리키는 값이 가리키는 주소 |
    | **pp | pp가 가리키는 값이 가리키는 값 |
- <정리>
    - 일반 변수 a를 함수에서 변경하려면 &a를 전달하고, int *p로 받는다
    - 포인터 변수 p를 함수에서 변경하려면 &p를 전달하고 int **p로 받는다

## 구조체

- 구조체
    
    ```c
    struct Student{
    	char name[20];
    	int score;
    };
    
    struct Student s;
    s.score = 90;
    ```
    
    - 서로 관련된 여러 데이터를 묶어 표현하는 사용자 정의 자료형
    - s : struct Student형 변수
    - s.score : 구조체 멤버에 접근
- 구조체 포인터
    
    ```c
    #include <stdio.h>
    
    struct Student{
    	char name[20];
    	int score;
    };
    
    int main(){
    	struct Student s = {"Kim", 80};
    	addScore(&s);
    	printf("%s %d\n", s.name, s.score);
    	return();
    }
    ```
    
    | 코드 | 의미 |
    | --- | --- |
    | struct Student | 구조체 변수 |
    | s.name | 구조체 변수의 멤버 접근 |
    | s.score | 구조체 변수의 멤버 접근 |
    | struct Student *p | 구조체 포인터 |
    | p = &s | s의 주소 저장 |
    | (*p).score | 포인터를 통해 멤버 접근 |
    | p → score | 위와 같은 의미 |
    | change(&s) | 구조체의 주소 전달 |

# 이진 탐색

#### “가운데를 기준으로 탐색 범위를 게속 절반을 나누는 방법”

```c
arr = 

index -> 0 1 2  3  4  5  6  7  8
value -> 3 7 12 18 25 31 42 56 68

target = 56
```

#### 규칙

1. arr[mid]와 target이 같다면 → 찾음
2. arr[mid]와 target보다 크다면 → high = mid - 1
3. arr[mid]와 target보다 작다면 → low = mid + 1

#### 알고리즘 작성

- 자연어
    
    ```c
    데이터는 현재 값 기준 왼쪽에 작은 값, 오른쪽에 큰 값으로 정렬되어 들어온다.
    
    배열 = 정렬된 데이터
    목표 = 하나의 정수값
    
    타겟을 찾을동안 반복
    	만약 비교결과가 같다면 True 반환
    	만약 비교결과가 목표보다 작다면 오른쪽으로 이동
    	만약 비교결과가 목표보다 크다면 왼쪽으로 이동
    ```
    
- 섞어서
    
    ```c
    low <- 0
    high <- 데이터 개수 -1
    
    low가 high보다 작거나 같을 동안 반복
    	mid <- (low + high) /2
    	if data[mid] = target
    		mid 반환
    	if data[mid] < target
    		low <- mid + 1
    	if data[mid] > target
    		high <- mid - 1
    ```
    

#### “이진 탐색은 정렬된 데이터에서 중간 값과 비교하여 탐색 범위를 절반씩 줄여가는 탐색 방법”

## 이중 연결 리스트

```c
<구조체>
struct node{
	int data;
	struct node * next;
	struct node * prev;
};
```

- 알고리즘 구상
    
    ```c
    입력 : head, size, target
    출력 : target이 있는 node 또는 nulld
    
    low <- 0
    high <- size -1
    
    current <- head
    currentIndex <- 0
    
    while low <= high
    	mid <- (low + high) / 2
    	while currentIndex < mid
    		current <- current.next
    		currentIndex <- currentIndex + 1
    	while currentIndex > mid
    		current <- current.prev
    		currentIndex <- currentIndex - 1
    	IF current.data == target
    		return current
    	else if current.data < target
    		low <- mid + 1
    	else
    		high <- mid -1
    		
    return null
    ```
    
- 전체 코드
    
    ```c
    //이중 연결 리스트 구현
    #include <stdio.h>
    #include <stdlib.h>
    typedef struct Node
    {
        int data;
        struct Node* prev;
        struct Node* next;
    } Node;
    
    // 메모리 해제
    void freeList(Node* head)
    {
        Node* current = head;
        while (current != NULL)
        {
            Node* temp = current;
            current = current->next;
            free(temp);
        }
    }
    
    // 이중 연결 리스트 이진 탐색
    Node* binarySearch(Node* head, int size, int target)
    {
        int low = 0;
        int high = size - 1;
    
        Node* current = head;
        int currentIndex = 0;
    
        while (low <= high) {
            int mid = (low + high) / 2;
    
            while (currentIndex < mid) {
                current = current->next;
                currentIndex = currentIndex + 1;
            }
            while (currentIndex > mid) {
                current = current->prev;
                currentIndex = currentIndex - 1;
            }
    
            if (current->data == target) {
                return current;
            }
            else if (current->data < target) {
                low = mid + 1;
            }
            else {
                high = mid - 1;
            }
        }
        return NULL;
    }
    
    // 맨 뒤에 노드 추가
    void insertBack(Node** head, int data, int* size)
    {
        Node* newNode = (Node*)malloc(sizeof(Node));
    
        newNode->data = data;
        newNode->prev = NULL;
        newNode->next = NULL;
    
        // 첫 번째 노드인 경우
        if (*head == NULL)
        {
            *head = newNode;
        }
        else
        {
            Node* current = *head;
    
            // 마지막 노드까지 이동
            while (current->next != NULL)
            {
                current = current->next;
            }
    
            current->next = newNode;
            newNode->prev = current;
        }
    
        (*size)++;
    }
    
    int main()
    {
        Node* head = NULL;
        int size = 0;
        int target;
    
        // 이진 탐색을 위해 정렬된 순서로 삽입
        insertBack(&head, 3, &size);
        insertBack(&head, 7, &size);
        insertBack(&head, 12, &size);
        insertBack(&head, 18, &size);
        insertBack(&head, 25, &size);
    
        printf("Enter a number to search: ");
        scanf("%d", &target);
    
        Node* result = binarySearch(head, size, target);
    
        if (result != NULL)
            printf("Found: %d\n", result->data);
        else
            printf("Not found.\n");
    
        freeList(head);
    
        return 0;
    }
    ```
    

# 정렬

#### “ 데이터를 일정한 기준에 따라 순서대로 배치하는 것”

## 선택 정렬

#### “남은 데이터에서 가장 작은 값을 선택하여 앞쪽으로 배치하는 방법”

- 알고리즘 작성
    1. (0번부터 시작) 가장 작은 값의 위치를 찾아서 0번 인덱스와 교환
        1. 0번째 인덱스 값이 가장 작은 값의 위치라고 가정
        2. 나머지 값들과 하나씩 비교
        3. 더 작은 값 발견 시 위치 변수의 값을 바꾼다
        4. 배열의 끝에 도달했다면 찾아낸 위치 변수와 0번째 값을 바꾼다
    2. 남은 배열에 대해서도 같은 작업 반복
- 코드
    
    ```c
    void selectionSort(int arr[], int n){
    	for(int i = 0; i < n - 1, i++){
    		int minIndex = i;
    		for(int j = i + 1; j < n; j++){
    			if(arr[j] < arr[minIndex]){
    				minIndex = j;
    				}
    			}
    		}
    		int temp = arr[i];
    		arr[i] = arr[minIndex];
    		arr[minIndex] = temp;
    	}
    }
    ```
    
- 정리
    
    ```c
    남은 데이터에서 -> 최솟값 선택 -> 현재 위치와 교환 -> 한 자리 확정 -> [정렬 완료][정렬X]
    
    i : 이번에 확정할 위치
    minIndex : 최솟값의 위치
    j : 최솟값을 찾기 위한 탐색
    
    시간 복잡도 -> O(n^2)
    ```
    

## 버블 정렬

#### 핵심

#### “인접한 두 값을 비교, 필요하면 교환. 이 과정을 반복하면 큰 값이 뒤쪽으로 이동”

#### “큰 값이 인접한 값과 계속 교환되면서 뒤쪽으로 올라가는 모습이 마치 거품이 올라가는것 같다고 해서 버블 정렬이라고 한다”

- 알고리즘
    
    ```c
    1. 비교할 두배열은 무엇인가?
    -> arr[i], arr[i+1]
    2. 교환조건
    -> arr[i] > arr[i+1]
    3. 교환
    temp = arr[i]
    arr[i] = arr[i+1]
    arr[i+1] = temp
    4. 반복 조건
    -> n-1
    5. 한바퀴로 정렬이 끝나나?
    -> 남은거 싹 다 반복
    ```
    
- 코드
    
    ```c
    void bubbleSort(int arr[], int n){
    	for(int i = 0; i < n-1; i++){
    		for(int j = i; j < n-1; j++){
    			if(arr[j] > arr[j+1]){
    				int temp = arr[j]
    				arr[j] = arr[j+1]
    				arr[j+1] = temp
    			}
    		}
    	}
    }
    ```
    

### 선택과 버블 정렬의 비교

|  | 선택 정렬 | 버블 정렬 |
| --- | --- | --- |
| 비교 | 남은 범위에서 최솟값 탐색 | 인접한 두 값 비교 |
| 교환 | 최솟값을 찾은 후 교환 | 순서가 다르면 비교 교환 |
| 확정 방향 | 앞 → 뒤 | 뒤 → 앞 |
| 한 회전 결과 | 최솟값 하나 확정 | 최댓값 하나 확정 |
| 시간 복잡도 | O(n^2) | O(n^2) |

→ 선택 정렬은 작은 값이 앞쪽부터 확정되고, 버블 정렬은 큰 값이 뒤로 간다.

## 삽입 정렬

#### “배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 부분 배열과 비교하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘”

- 자연어
    
    ```c
    1. 처음부터 몇 번쨰 원소까지는 정렬되어있다고 볼 수 있을까?
    
    → 0번째
    
    2. 정렬을 시작할 원소 : 1번째
    3. 이번에 정렬된 부분에 넣을 값을 어떻게 해야할까?
    
    → 따로 저장, key 변수
    
    4. 어느 방향으로 비교해야 할까?
    
    → 왼쪽(감소)
    
    5. 앞의 값이 현재 값보다 크면 어떻게 해야할까?
    
    → 오른쪽으로 이동(1칸)
    
    6. 현재 값이 더 클때 or 배열 제일 앞일때 비교를 멈춘다
    7. 비교후 비어 있는 위치에 현재 값 삽입
    8. 배열의 끝에서 정렬을 멈춘다
    ```
    
- 알고리즘
    
    ```c
    삽입 정렬(A, n)
    
    for i <- i to n-1
    	key <- A[i]
    	j <- i - 1
    	while A[j] > key & j >= 0
    		A[j+1] <- A[j]
    		j = j -1
    	A[j+1] <- key
    ```
    
- 코드
    
    ```c
    void insetSort(int arr[], int n){
    	for(int i = 1; i < n; i++){
    		int key = A[i]
    		int j = i - 1
    		while(A[j] > key && j != 0){
    			A[j+1] = A[j]
    			j -= 1
    			}
    		A[j+1] = key
    ```
    

### 선택, 버블, 삽입 총 정리(내림차순 기준)

|  | 선택 | 버블 | 삽입 |
| --- | --- | --- | --- |
| 핵심 아이디어 | 가장 작은 값 선택 | 이웃한 값을 비교 | 정렬된 부분에 값 삽입 |
| 한 단계가 끝나면 | 작은 값이 앞쪽에 확정 | 큰 값이 뒤쪽에 확정 | 왼쪽의 정렬된 영역이 확장 |
| 주요 동작 | 비교+탐색+교환 | 비교+교환 | 비교+이동+삽입 |
| 평균 시간 복잡도 | O(n^2) | O(n^2) | O(n^2) |
| 추가 배열 필요 여부 | X  | X | X |

# 해시

## 해시 함수

#### 용어 정리

해싱 : 키를 해시 함수에 넣어 저장 위치를 결정하는 과정/기법

키(key) : 찾거나 저장하려는 데이터를 구별하는 값

해시 함수 : key를 이용하여 저장할 위치를 계산하는 함수

해시 테이블 : 해시 함수로 계산한 위치에 데이터를 저장하는 자료구조

- 알고리즘
    1. 함수에 전달 받아야 하는 값을 무엇인가
    
    → key
    
    1. 함수가 반환해야 하는 값
    
    → index
    
    1. index는 어떻게 계산하는가
    
    → key % 테이블 크기
    
- 코드
    
    ```c
    #define Table_Size 10
    
    int table[Table_Size]
    int hash(int key){
    	return key % Table_Size;
    }
    ```
    
- 해시 탐색
    
    
    | 탐색 | 탐색 방법 | 시간 복잡도 |
    | --- | --- | --- |
    | 순차 | 하나씩 확인 | O(n) |
    | 이진 | 범위를 절반씩 줄임 | O(log n) |
    | 해시 | 위치를 계산하여 접근 | O(1) → 평균 |
- 충돌
    
    → 서로 다른 key가 해시 함수에 의해서 같은 저장 위치를 가지게 되는 현상
    
    발생 이유
    
    → 인덱스는 유한한데 키는 무수히 만들 수 있기 때문
    
    <데이터 추가 조건>
    
    1. 기존 데이터 삭제 x
    2. 모든 데이터는 나중에 다시 찾을 수 있어야함

## 체이닝

#### “같은 index를 가지는 데이터들을 연결하여 저장하는 충돌 해결 방법”

- 구조체
    
    ```c
    #define Table_Size 10
    struct Node{
    	int key;
    	struct Node * next;
    }
    
    Struct Node * table[Table_Size];
    
    #해시 테이블 : 배열 + 각 배열 요소에서 시작되는 연결 리스트
    ```
    
- 초기화 코드
    
    ```c
    void initTable(){
    	for(int i = 0; i < Table_Size; i++){
    		table[i] = NULL;
    	}
    }
    ```
    
- 삽입 알고리즘
    
    ```c
    //삽입
    -> index 계산
    -> 새 노드 생성
    -> key값 저장
    
    insert(key)
    1. key의 인덱스 계산 hash(key)
    2. 새로운 노드 생성 * 포인터
    -> new node.key = key
    -> new node.next = table[index]
    -> table[index] = new node
    ```
    
- 삽입 코드
    
    ```c
    
    void insert(int key){
    	int index = hash(key);
    	struct node * new Node = malloc(sizeof(struct Node));
    	new Node -> key = key;
    	(*new node).next = tablep[index]
    	table[index] = new Node;
    }
    ```
    
- 정리
    1. 해시 함수를 이용하여 키가 저장될 인덱스를 계산
    2. 새로운 노드 생성
    3. 새로운 노드에 키를 저장
    4. 새로운 노드의 next가 기존 table[index]를 가리키게 한다
    5. table[index]가 새로운 Node를 가리키게 한다

## 탐색과 삭제

- 탐색 알고리즘
    
    ```c
    SERACH(key)
    index <- hash(key)
    current <- table[index]
    
    WHILE current != NULL
    	IF current -> key == key
    		return current
    	current <- (current -> next)
    return NULL
    ```
    
    ```c
    serach(key)
    1. hash(key)를 이용하여 index 계산
    2. table[index]의 첫번째 Node에서 시작
    3. 현재 Node의 key와 찾으려는 key를 비교
    4. 같으면 현재 Node를 반환
    5. 다르면 다음 Node로 이동
    6. Null에 도달할 때까지 반복
    7. 끝까지 찾지 못하면 NULL을 반환
    ```
    
- 탐색 코드
    
    ```c
    struct Node * search(int key){
    	int index = hash(key);
    	current = table[index];
    	while(current != NULL){
    		IF(current -> key == key){
    			return current;
    		}
    		current = current -> next;
    	}
    	return NULL
    }
    ```
    
- 삭제 알고리즘
    
    ```c
    DELETE(key)
    index <- hash(key)
    current <- table[index]
    prev <- NULL
    
    WHILE current != NULL && current != key
    	prev <- current
    	current <- current -> next
    	IF current가 존재하지 않으면
    		return
    	IF prev가 존재하지 않으면
    		table[index] = current -> next
    	ELSE
    		prev -> next = current next
    	FREE current
    ```
    
    ```c
    1. 해시 함수를 이용하여 key가 저장되어 있을 index를 계산한다.
    2. 해당 index의 첫번째 노드부터 확인한다.
    3. key가 일치할때까지 이전 노드와 현재 노드를 이동한다.
    4. 끝까지 찾지 못했다면 삭제하지 않고 종료한다.
    5. 찾은 노드가 첫번째 노드라면 table[index]가 다음 노드를 가리키도록 연결
    6. 삭제할 노드의 메모리를 해제한다.
    ```
    
- 삭제 코드
    
    ```c
    struct node * delete(int key){
    	int index = hash(key);
    	struct node * current = table[index];
    	struct node * prev = NULL;
    	WHILE(current != NULL && current.key != key){
    		prev = current;
    		current = current -> next;
    		IF(current == NULL){
    			table[index] = current -> next;
    		}
    		IF(prev == NULL){
    			prev -> next = current -> next;
    		}
    		ELSE{
    			prev -> next = current -> next;
    		}
    	FREE current;
    }
    ```
    

해시 Big-O : O(n), O(1)

충돌이 거의 없을 때 : O(1)

충돌이 아주 많을 때 : O(n)

체이닝을 사용하는 해시 탐색은 평균 O(1)이지만, 최악의 경우 O(n)까지 느려질 수 있다.

## 함수 정리와 해제

- 해제 알고리즘
    
    ```c
    table의 각 index를 순회
    -> 연결 리스트의 모든 Node 순회
    -> 하나씩 Free()
    ```
    
- 해제 코드
    
    ```c
    void freeTable(){
    	for(int i = 0; i < Table_Size; i++){
    		struct Node * current = table[i];
    		while(current != NULL){
    			struct Node * temp = current;
    			current = current -> next;
    			free(temp);
    		}
    		table[i] = NULL;
    	}
    }
    ```
    
- 함수정리
    
    
    | 함수 | 역할 |
    | --- | --- |
    | int hash(int key) | key가 저장될 index 계산 |
    | void initTable() | 모든 table[index[을 Null로 초기화 |
    | void insert(int key) | key 삽입 |
    | struct Node * serach(int key) | key 탐색 |
    | void deleteKey(int key) | key 삭제 |
    | void freeTable() | 모든 노드 메모리 해제 |

# 해시_개방 주소법

#### “충돌이 발생했을 때 해시 테이블 내부의 다른 빈 위치를 찾아 저장하는 방법”

- 삽입 알고리즘
    
    ```c
    INSERT(key)
    	index <- hash(key)
    	count <- 0
    	WHILE count < Table_Size
    		if table[index] != 0
    			table[index] = key
    			return
    		index <- (index + 1) % Table_Size
    		count <- count + 1
    	테이블 가득 참 출력
    ```
    
- 삽입 코드
    
    ```c
    void insert(int key){
    	int index = hash(key);
    	int count = 0;
    	while(count < Table_Size){
    		if(table[index] == EMPTY){
    			table[index] = key;
    			return;
    		}
    		index = (index + 1) % Table_Size;
    		count = count + 1
    	printf("테이블이 가득 참");
    ```
    
- 탐색 알고리즘
    
    ```c
    SEARCH(key)
    	index <- hash(key)
    	count <- 0
    	while count < Table_Size
    		if table[index] == key
    			return index
    		if table[index] == EMPTY
    			return -1
    		index <- (index + 1) % Table_Size
    		count <- count + 1
    	return -1
    ```
    
    ```c
    탐색 시작 -> hash(key), index
    현재 위치에 찾는 key가 있다면? -> 성공
    다른 값이 있다면? -> 다음 위치, index + 1
    배열에 끝에 도달 했다면? -> 처음으로 돌아감
    언제 없다고 판단? -> count, EMPTY
    ```
    
- 탐색 코드
    
    ```c
    int search(int key){
    	int index = hash(key);
    	int count = 0;
    	while(count < Table_Size){
    		if(table[index] == key){
    			return index;
    		}
    		if(table[index] == EMPTY){
    			return -1;
    		}
    		index = (index + 1) % Table_Size;
    		count += 1;
    		}
    	return -1
    ```
    

## EMPTY의 문제점 보완

| 값 | 의미 |
| --- | --- |
| EMPTY | 한번도 사용하지 않은 공간 |
| DELETED | 데이터가 있었지만 삭제된 공간 |
| 그외 값 | 실제 저장된 key |
- 보완된 삭제 알고리즘
    
    ```c
    DLETE(key)
    	index <- hahs(key)
    	count <- 0
    	while count < Table_Size
    		if table[index] == key
    			table[index] = DELETED
    			return
    		if table[index] == EMPTY
    			return
    		index <- (index + 1) % Table_Size
    		count <- count + 1
    ```
    
    !image.png
    
- 보완된 삭제 코드
    
    ```c
    void delete(int key){
    	int index = hash(key);
    	int count = 0;
    	wihle(count < Table_Size){
    		if(table[index] == key){
    			table[index] == DELETED;
    			return;
    		}
    		if(table[index] == EMPTY){
    			return;
    		}
    		index = (index + 1) % Table_Size;
    		count += 1;
    	}
    ```
    
- 삽입 보완과 바뀐점
    
    ```c
    함수명 : insert
    수정 전 : if(table[index] == EMPTY)
    수정 후 : if(table[index] == EMPTY) || table[index] == DELETED)
    ```
    
    | 현재 위치 | INSERT | SERACH | DELETE |
    | --- | --- | --- | --- |
    | 원하는 key | - | 성공 return | DELETED로 변경 |
    | 다른 key | 다음 위치 | 다음 위치 | 다음 위치 |
    | EMPTY | 저장 | 탐색 종료 | 삭제 종료 |
    | DELETED | 저장 | 계속 탐색 | 계속 탐색 |

## 군집화

#### “데이터가 모이는 현상”

Linear Probing에서 이렇게 연속된 큰 덩어리가 형성되는 현상을 1차 군집화라고 한다.

왜 군집이 점점 커질까?

군집 발생 → 충돌 가능성 증가 → 새로운 데이터가 군집뒤에 저장 → 군집이 더 커짐 → 다시 충돌 증가

해결 

→ 2차 조사법 : 이동 간격 변경(제곱의 형태로, (1, 4, 9…)

- 이중 해싱
    
    !image.png
    

## 세가지 조사법 정리

#### 선형 조사법

- 충돌 → 다음칸 → 다음칸 → 다음칸
- 특징 : 구현이 단순
- 문제 : 1차 군집화 발생가능

#### 2차 조사법

- 충돌 → + 1^2 → + 2^2 → + 3^2
- 특징 : 조사 간격 변화
- 목적 연속된 군집 줄임
- 남은 문제 : 같은 초기 해시값이면 같은 조사 순서를 사용

#### 이중 해싱

충돌 → 두번째 해시함수

→ key에 따른 다른 간격으로 조사 → (h1(key) + i * h2(key)) % 테이블 크기

특징 : key에 따라 조사 순서를 더 다양하게 만들 수 있음

## 체이닝과 개방 주소법 비교

| 비교 항목 | 체이닝 | 개방 주소법 |
| --- | --- | --- |
| 충돌 발생 시 | 같은 위치에 연결 | 다른 빈 위치 탐색 |
| 데이터 저장 | 연결된 노드 사용 | 테이블 내부에 저장 |
| 추가 자료구조 | 연결 리스트 등 필요 | 기본적으로 필요 없음 |
| 테이블이 가득 찬 경우 | 추가 노드를 연결할 수 있음 | 빈 공간이 없으면 삽입 불가 |
| 충돌이 많아질 경우 | 체인이 길어짐 | 군집화를 고려해야함 |
| 삭제 | 연결 관계를 수정 | 삽입을 고려해야함 |
| 대표적인 성능 문제 | 긴 체인 | 군집화 |

# DFS & BFS

### 그래프 : 정점과 간선으로 구성된 자료구조

G = (V, E), V : 정점의 집합, E : 간선의 집합

- 그래프의 종류
    - 무방향
    - 방향
    - 가중치

컴퓨터는 그래프를 어떻게 저장할까?

1. 메모리에 그래프를 그림 형태로 저장할 수 없다.
2. 그래프의 연결관계를 인접행렬, 리스트로 표현한다.
- 인접행렬과 리스트 예시
    
    !image.png
    
    !image.png
    
- 인접 행렬과 리스트 비교
    - 정점 대비 간선이 많을때 → 인접 행렬(접근이 빠르다)
    
    |  | 인접 행렬 | 인접 리스트 |
    | --- | --- | --- |
    | 표현 | 2차원 배열 | 연결된 정점 목록 |
    | 공간 복잡도 | O(V^2) | O(V+E) |
    | 두 정점 연결 확인 | 빠름 | 탐색 필요 |
    | 간선이 많은 그래프 | 적합 | 가능 |
    | 간선이 적은 그래프 | 공간 낭비, 가능 | 적합 |
    - 그래프 탐색
        - 시작 정점에서 간선을 따라 이동하며, 도달할 수 있는 정점들을 체계적으로 방문하는 과정
    - 왜 탐색이 필요한가
        - 두 정점 사이에 이동 가능한 경로가 있는지 확인하기 위해
        - 시작 정점과 연결된 정점들을 찾기위해
        - 조건에 맞는 경로를 찾기 위해

## DFS(Depth First Serach)

그래프에서 한 방향으로 가능한 깊이까지 탐색한 뒤, 더 이상 방문할 정점이 없으면 이전 정점으로 돌아가 다른 방향을 탐색하는 방법

!image.png

- 방문 순서 : 0 → 1 → 3 → 2 → 4
- 방문 여부 저장 안할시
    - 사이클(반복) 발생 할 수 있음
- 의사코드
    
    ```c
    DFS(v)
    visited[v] <- 1
    모든 정점 i에 대하여 
    	만약 v와 i가 연결되어있고
    		i를 아직 방문하지 않았다면
    			DFS(i)
    ```
    
- 코드
    
    ```c
    void dfs(int v, int n, int table[n][n]){
        visited[v] = 1;
        for(int i = 0; i < n; i++){
            if(visited[i] == 0 && table[v][i] == 1){
                dfs(i, n, table);
            }
        }
    }
    ```
    

## BFS(Breadth First Serach)

시작 정점과 가까운 정점부터 방문하고, 점차 더 멀리 있는 정점으로 탐색 범위를 넓혀가는 방법

!image.png

- 방문 순서 : 0 → 1 → 2 → 4 → 3
- 의사 코드
    
    ```c
    BFS(start)
    	visited[start] <- 1
    	start를 Queue에 삽입
    	Queue가 비어있지 않은 동안
    		v <- Queue에서 삭제
    		모든 정점 i에 대하여
    			만약 v와 i가 연결 되어 있고
    			i를 아직 방문하지 않았다면 
    				visited[i] = 1;
    				i를 Queue에 삽입
    ```
    
- 코드
    
    ```c
    void bfs(int start){
        int queue[V];
        int front = 0;
        int rear = 0;
    
        visited[start] = 1;
        queue[rear++] = start;
        while(front < rear){
            int v = queue[front++];
            printf("%d ", v);
            for(int i = 0; i < V; i++){
                if(graph[v][i] && !visited[i]){
                    visited[i] = 1;
                    queue[rear++] = i;
                }
            }
        }
    }
    ```
    

## 비교

DFS : 정점을 방문하면, 바로 그 정점으로 이동(재귀, 스택)

BFS : 현재 정점과 가까운 정점들을 먼저 처리(큐)

|  | DFS | BFS |
| --- | --- | --- |
| 의미 | 깊이 우선 탐색 | 너비 우선 탐색 |
| 탐색 방식 | 한 방향으로 깊게 | 가까운 정점부터 |
| 핵심 자료구조 | Stack/재귀 | Queue |
| 방문 기록 | visited | visited |
| 그래프 전체 탐색 | 가능  | 가능 |

# 다익스트라

#### “음수 가중치가 없는 가중치 그래프에서 하나의 출발 정점으로부터 다른 모든 정점까지의 최단 거리를 구하는 알고리즘

다익스트라 알고리즘 핵심

1. 아직 처리하지 않은 정점 중 현재 거리가 가장 짧은 정점을 선택한다.
2. 그 정점을 거쳐가는 것이 더 짧다면 거리를 갱신한다.
- 시간 복잡도 : O(n^2), n : 정점 수

dist에서의 INF  = 발견 X

grape에서의 INF = 연결 X

- 에시
    
    !image.png
    
- 알고리즘
    
    ```c
    출발 정점의 거리 -> 0
    나머지 정점의 거리 처음은, 방문 여부는 -> INF, visited[]로 관리
    다음 정점은 어떤 기준으로 선택하는가 -> 방문하지 않은 정점 중 dist[]가 가장 작은 정점
    정점을 선택한 후 하는 일은 -> 선택한 정점과 연결된 정점 확인
    언제 거리를 변경하는가 -> 선택한 정점을 거쳐가는 경로가 기존 거리보다 짧을때
    이미 처리한 정점은 다시 선택하는가 -> X
    ```
    
    ```c
    for i <- 0 to n - 1
    
    	dist[i] <- INF
    	visited[i] <- 0
    	
    dist[start] <- 0
    for count <- 0 to n - 1
    	u <- findMinVertex(dist, visited)
    	visited[u] <- 1
    	
    	for v <- 0 to n - 1
    		if graph[u][v] != INF AND visited[v] = 0
    			if dist[u] + graph < dist[v]
    				dist[v] <- dist[u] + graph[u][v]
    ```
    

| 자료 | 저장하는것 |
| --- | --- |
| graph[][] | 정점 사이의 직접적인 가중치 |
| dist[] | 시작 정점에서 각 정점에서 현재까지 발견한 최단 거리 |
| visited[] | 해당 정점을 선택하여 처리했는지에 대한 여부 |
- 배열 초기화 코드
    
    ```c
    for(int i = 0; i < n; i++){
    	dist[i] = INF;
    	visited[i] = 0;
    }
    dist[start] = 0;
    ```
    
- 가장 작은 정점의 인덱스 반환 알고리즘
    - 아직 처리하지 않은 정점 중 dist[] 값이 가장 작은 정점의 인덱스를 반환
    
    ```c
    알고리즘
    1. 모든 N을 확인한다.
    2. 아직 처리되지 않은 조건 + 현재까지 찾은 최소 거리보다 작으면
    3. 최소 인덱스를 바꾼다.
    4. 모든 반복이 끝나면 최종적으로 정점 번호를 반환한다.
    ```
    
    ```c
    findMinVertex(dist, visited)
    min <- INF
    minIndex <- -1
    
    for i <- 0 to n - 1
    	if min > dist[i] && visited == 0
    		min <- dist[i]
    		minIndex <- i
    return minIndex
    ```
    
- 가장 작은 정점의 인덱스 반환 코드
    
    ```c
    int findMinVertex(int dist[N], int visited[N]){
        int min = INF;
        int minIndex = -1;
    
        for(int i = 0; i < N; i++){
            if(min > dist[i] && visited[i] == 0){
                min = dist[i];
                minIndex = i;
            }
        }
        return minIndex;
    }
    ```
    
- 다익스트라 알고리즘과 코드
    - 만약 시작 정점에서 더 이상 도달할 수 있는 미바문 정점이 없다면 findMinVertext()는 -1을 반환하는데 이때 visited[-1] = 1을 실행하면 잘못된 접근 오류 발생
    - 안전을 위해 X 코드를 추가
    
    ```c
    void Dijkstra(int start){
        for(int i = 0; i < N; i++){
            dist[i] = INF;
            visited[i] = 0;
        }
        dist[start] = 0;
        for(int count = 0; count < N; count++){
            int u = findMinVertex(dist, visited);
            if(u == -1) break; -> X
            visited[u] = 1;
            for(int v = 0; v < N; v++){
                if(graph[u][v] != INF && visited[v] == 0){
                    if(dist[u] + graph[u][v] < dist[v]){
                        dist[v] = dist[u] + graph[u][v];
                    }
                }
            }
        }
    }
    
    ```
    
- 최단 거리 출력
    
    ```c
    printf("출발 장소: %s\n\n", places[start]);
        for(int i = 0; i < N; i++){
            if(dist[i] == INF){
                printf("%s : INF\n",  places[i]);
            }
            else{
                printf("%s : %d분\n", places[i], dist[i] * 10);
            }
        }
    ```