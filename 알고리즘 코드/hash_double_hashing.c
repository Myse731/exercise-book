#include <stdio.h>
#define TABLE_SIZE 7
#define EMPTY -1
#define DELETED -2

int table[TABLE_SIZE];

void init_table(){
    for(int i = 0; i < TABLE_SIZE; i++){
        table[i] = EMPTY;
    }
}

int h1(int key) {
    return key % TABLE_SIZE;
}

int h2(int key){
    return 1 + (key % (TABLE_SIZE - 1));
}

int hash(int key, int count){
    return (h1(key) + count * h2(key)) % TABLE_SIZE;
}

int search(int key){
    for(int count = 0; count < TABLE_SIZE; count++){
        int index = hash(key, count);
        if(table[index] == key){
            return index;
        }
        if(table[index] == EMPTY){
            return -1;
        }
    }
    printf("Not Found");
    return -1;
}
int probeIndex(int key, int count){
    return hash(key, count);
}

void insert(int key){
    if(search(key) != -1){
        printf("%d : already exists.\n", key);
        return;
    }

    for(int count = 0; count < TABLE_SIZE; count++){
        int index = probeIndex(key, count);

        if(table[index] == EMPTY || table[index] == DELETED){
            table[index] = key;
            printf("%d: inserted at index %d.\n", key, index);
            return;
        }
    }
    printf("Hash table is full.\n");
}


void delete(int key){
    for(int count = 0; count < TABLE_SIZE; count++){
        int index = hash(key, count);
        if(table[index] == key){
            table[index] = DELETED;
            printf("%d: deleted from index %d.\n", key, index);
            return;
        }
        if(table[index] == EMPTY){
            return;
        }
    }
}

int main(){
    init_table();

    printf("=== [1] 삽입 및 가득 차는 과정 테스트 ===\n");
    insert(22);
    insert(32);
    insert(42);
    insert(52);
    insert(62);
    insert(72);
    insert(82);

    printf("\n=== [2] 탐색 테스트 ===\n");
    int target = 42;
    int idx = search(target);
    if(idx != -1) printf("키 %d 탐색 성공 -> 인덱스: %d\n", target, idx);
    else printf("키 %d 탐색 실패\n", target);

    printf("\n=== [3] 삭제 및 DELETED 통과 탐색 테스트 ===\n");
    delete(32);

    idx = search(72);
    if(idx != -1) printf("32 삭제 후에도 키 72 정상 탐색 성공 -> 인덱스: %d\n", idx);
    else printf("키 72 탐색 실패\n");

    return 0;
}