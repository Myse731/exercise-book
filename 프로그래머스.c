#include <stdio.h>

int main(void) {
    int a;
    scanf("%d", &a);
    if(a % 2 == 0){
        printf("%d is even", a);
    }
    else{
        printf("%d is odd", a);
    }
    return 0;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int len = strlen(my_string);
    
    int start = len - n;
    
    char* answer = (char*)malloc(n+1);
    int idx = 0;
    for(int j = start; j < len; j++){
        answer[idx] = my_string[j];
        idx ++;
    }
    answer[idx] = '\0';
    return answer;
}

#include <stdio.h>
#define LEN_INPUT1 11
#define LEN_INPUT2 11

int main(void) {
    char s1[LEN_INPUT1];
    char s2[LEN_INPUT2];
    scanf("%s %s", s1, s2);
    printf("%s%s", s1, s2);

    return 0;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int number, int n, int m) {
    int result = 0;
    if(number % n == 0 && number % m == 0){
        result = 1;
    }
    else{
        result = 0;
    }
    return result;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* n_str) {
    int result = 0;
    for(int i = 0; i < strlen(n_str); i++){
        result = result * 10 + (n_str[i] - '0');
    }
    return result;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b) {
    int count1 = 1;
    int count2 = 1;
    
    int result = 0;
    int temp_b = b;
    
    while(temp_b > 0){
        count1 *= 10;
        temp_b /= 10;
    }
    
    int temp_a = a;
    while(temp_a > 0){
        count2 *= 10;
        temp_a /= 10;
    }
    int result1 = a * (count1) + b;
    int result2 = b * (count2) + a;
    
    if(result1 >= result2){
        result = result1;
    }
    else{
        result = result2;
    }
    return result;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int* solution(int num_list[], size_t num_list_len, int n) {
    int* answer = (int*)malloc(sizeof(int) * (num_list_len - n + 1));
    int idx = 0;
    for(int i = n - 1; i < num_list_len; i++){
        answer[idx] = num_list[i];
        idx++;
    }
    return answer;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int* solution(int num_list[], size_t num_list_len, int n) {
    int* answer = (int*)malloc(sizeof(int) * (num_list_len - 1) / n + 1);
    int idx = 0;
    for(int i = 0; i < num_list_len; i += n){
        answer[idx] = num_list[i];
        idx++;
    }
    return answer;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, int k) {
    int idx = 0;
    char* answer = (char*)malloc(sizeof(char) * (strlen(my_string) * k + 1));
    for(int i = 0; i < k; i++){
        for(int j = 0; j < strlen(my_string); j++){
            answer[idx] = my_string[j];
            idx++;
        }
        answer[idx] = '\0';
    }
    return answer;
}

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* my_string, const char* target) {
    int len_my = strlen(my_string);
    int len_tg = strlen(target);

    for(int i = 0; i <= len_my - len_tg; i++){
        bool ismatch = true;
        for(int j = 0; j < len_tg; j++){
            if(my_string[i + j] != target[j]){
                ismatch = false;
                break;
            }
        }
        if(ismatch){
        return 1;
        }
    }
    return 0;
}