#include <stdio.h>
#include <stdlib.h>

#define TABLE_SIZE 12

struct Node {
    int key;
    struct Node * next;
};

struct Node * table[TABLE_SIZE];

int hash(int key) {
    int index = key % TABLE_SIZE;
    if (index < 0) index += TABLE_SIZE;
    return index;
}

void initTable() {
    for(int i = 0; i < TABLE_SIZE; i++) {
        table[i] = NULL;
    }
}

void printTable() {
    for(int i = 0; i < TABLE_SIZE; i++) {
        printf("[%d]", i);
        
        struct Node * current = table[i];
        while(current != NULL) {
            printf(" -> %d", current->key);
            current = current->next;
        }
        printf(" -> NULL\n");
    }
}

void insert(int key) {
    int index = hash(key);
    struct Node * newNode = (struct Node *)malloc(sizeof(struct Node));
    if (newNode == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return;
    }
    
    newNode->key = key;
    newNode->next = table[index];
    table[index] = newNode;
}

struct Node * search(int key) {
    int index = hash(key);
    struct Node * current = table[index];
    while(current != NULL) {
        if(current->key == key) {
            return current;
        }
        current = current->next;
    }
    return NULL;
}

void delete(int key) {
    int index = hash(key);
    struct Node * current = table[index];
    struct Node * prev = NULL;
    
    while(current != NULL && current->key != key) {
        prev = current;
        current = current->next;
    }
    
    if(current == NULL) {
        return;
    }
    
    if(prev == NULL) {
        table[index] = current->next;
    } else {
        prev->next = current->next;
    }
    free(current);
}

void freeTable() {
    for(int i = 0; i < TABLE_SIZE; i++) {
        struct Node* current = table[i];
        while(current != NULL) {
            struct Node* temp = current;
            current = current->next;
            free(temp);
        }
        table[i] = NULL;
    }
}

int main() {
    initTable();
    insert(1);
    insert(2);
    insert(4);
    insert(13);
    insert(25);
    insert(16);
    insert(28);

    printf("=== After Insert ===\n");
    printTable();

    printf("=== Search 25 ===\n");
    struct Node * res = search(25);
    if(res != NULL) {   
        printf("Found : %d\n", res->key);
    } else {
        printf("Not Found\n");
    }

    printf("=== Search 99 ===\n");
    res = search(99);
    if(res != NULL) {
        printf("Found : %d\n", res->key);
    } else {
        printf("Not Found\n");
    }

    printf("=== Delete 25 ===\n");
    delete(25);
    printTable();

    printf("=== Delete 16 ===\n");
    delete(16);
    printTable();

    printf("=== Delete 99 ===\n");
    delete(99);
    printTable();

    freeTable();
    printf("=== free Table ===\n");
    printTable();
    return 0;
}