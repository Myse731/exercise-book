#include <stdio.h>

int chars(char * arr){
    int sum = 0;
    while(*(arr++) != '\0'){
        sum += 1;
    }

    return sum;
}

void pal(char * arr){
    char arr2[11];

    int len = chars(arr);

    for(int i = 0; i < len; i++){
        *(arr2 + len -1 -i) = *(arr + i);
    }

    arr2[len] = '\0';

    int same = 1;

    for(int i = 0; i < len; i++){
        if(*(arr2 + i) == *(arr + i)){
            same = 0;
            break;
        }
    }

    if(same == 1){
        printf("palindrome");
    }
    else{
        printf("not palindrome");
    }
}


int main(void){
    char arr[11];

    scanf("%10s", arr);

    pal(arr);
}