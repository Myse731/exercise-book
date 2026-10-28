#define TABLE_SIZE 7
#define EMPTY -1
#define DELETED -2

int table[TABLE_SIZE];

void init_table(){
    for(int i = 0; i < TABLE_SIZE; i++){
        table[i] = EMPTY;
    }
}

void insert(int key){
    int index = hash(key);
    int count = 0;
    while(count < TABLE_SIZE){
        if(table[index] == EMPTY || table[index] == DELETED){
            table[index] = key;
            return;
        }
        index = (index + 1) % TABLE_SIZE;
        count++;
    }
    printf("테이블이 가득참");
}

int search(int key){
    int index = hash(key);
    int count = 0;
    while(count < TABLE_SIZE){
        if(table[index] == key){
            return index;
        }
        if(table[index] == EMPTY){
            return -1;
        }
        index = (index + 1) % TABLE_SIZE;
        count++;
    }
    return -1;
}

void delete(int key){
    int index = hash(key);
    int count = 0;
    while(count < TABLE_SIZE){
        if(table[index] == key){
            table[index] = DELETED;
            return;
        }
        if(table[index] == EMPTY){
            return;
        }
        index = (index + 1) % TABLE_SIZE;
        count++;
    }
}

