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
        1. 첫번쨰 원소부터 확인
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