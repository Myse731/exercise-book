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
    return 1 + (key % (TABLE_SIZE));
}

int hash(int key, int count){
    return (h1(key) + count * h2(key) % TABLE_SIZE);
}

int probelIndex(int key, int count){

}

void insert(int key){
    if(serach(key) != -1){
        printf("%d : aleady exists.\n", key);
        return;
    }

    for(int count = 0; count < TABLE_SIZE; count++){
        int index = probelIndex(key, count);

        if(table[index] == EMPTY || table[index] == DELETED){
            table[index] = key;
            printf("%d: inserted at index %d.\n", key, index);
            return;
        }
    }
    printf("Hash table is full.\n");
}

int search(int key){
    for(int count = 0; count < TABLE_SIZE; count++){
        int index = hash(key, count);
        if(table[index] == key){
            return index;
        }
        if(table[index] == EMPTY || table[index] == DELETED){
            return -1;
        }
        index = (index + 1) % TABLE_SIZE;
    }
    return -1;
}

void delete(int key){
    for(int count = 0; count < TABLE_SIZE; count++){
        int index = hash(key, count);
        if(table[index] == key){
            table[index] == DELETED;
            return;
        }
        if(table[index] == EMPTY){
            return;
        }
        index = (index + 1) % TABLE_SIZE;
    }
}