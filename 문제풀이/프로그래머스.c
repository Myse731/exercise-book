// #include <stdio.h>

// int main(void) {
//     int a;
//     scanf("%d", &a);
//     if(a % 2 == 0){
//         printf("%d is even", a);
//     }
//     else{
//         printf("%d is odd", a);
//     }
//     return 0;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* my_string, int n) {
//     // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
//     int len = strlen(my_string);
    
//     int start = len - n;
    
//     char* answer = (char*)malloc(n+1);
//     int idx = 0;
//     for(int j = start; j < len; j++){
//         answer[idx] = my_string[j];
//         idx ++;
//     }
//     answer[idx] = '\0';
//     return answer;
// }

// #include <stdio.h>
// #define LEN_INPUT1 11
// #define LEN_INPUT2 11

// int main(void) {
//     char s1[LEN_INPUT1];
//     char s2[LEN_INPUT2];
//     scanf("%s %s", s1, s2);
//     printf("%s%s", s1, s2);

//     return 0;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int number, int n, int m) {
//     int result = 0;
//     if(number % n == 0 && number % m == 0){
//         result = 1;
//     }
//     else{
//         result = 0;
//     }
//     return result;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// int solution(const char* n_str) {
//     int result = 0;
//     for(int i = 0; i < strlen(n_str); i++){
//         result = result * 10 + (n_str[i] - '0');
//     }
//     return result;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int a, int b) {
//     int count1 = 1;
//     int count2 = 1;
    
//     int result = 0;
//     int temp_b = b;
    
//     while(temp_b > 0){
//         count1 *= 10;
//         temp_b /= 10;
//     }
    
//     int temp_a = a;
//     while(temp_a > 0){
//         count2 *= 10;
//         temp_a /= 10;
//     }
//     int result1 = a * (count1) + b;
//     int result2 = b * (count2) + a;
    
//     if(result1 >= result2){
//         result = result1;
//     }
//     else{
//         result = result2;
//     }
//     return result;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // num_list_len은 배열 num_list의 길이입니다.
// int* solution(int num_list[], size_t num_list_len, int n) {
//     int* answer = (int*)malloc(sizeof(int) * (num_list_len - n + 1));
//     int idx = 0;
//     for(int i = n - 1; i < num_list_len; i++){
//         answer[idx] = num_list[i];
//         idx++;
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // num_list_len은 배열 num_list의 길이입니다.
// int* solution(int num_list[], size_t num_list_len, int n) {
//     int* answer = (int*)malloc(sizeof(int) * (num_list_len - 1) / n + 1);
//     int idx = 0;
//     for(int i = 0; i < num_list_len; i += n){
//         answer[idx] = num_list[i];
//         idx++;
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* my_string, int k) {
//     int idx = 0;
//     char* answer = (char*)malloc(sizeof(char) * (strlen(my_string) * k + 1));
//     for(int i = 0; i < k; i++){
//         for(int j = 0; j < strlen(my_string); j++){
//             answer[idx] = my_string[j];
//             idx++;
//         }
//         answer[idx] = '\0';
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// int solution(const char* my_string, const char* target) {
//     int len_my = strlen(my_string);
//     int len_tg = strlen(target);

//     for(int i = 0; i <= len_my - len_tg; i++){
//         bool ismatch = true;
//         for(int j = 0; j < len_tg; j++){
//             if(my_string[i + j] != target[j]){
//                 ismatch = false;
//                 break;
//             }
//         }
//         if(ismatch){
//         return 1;
//         }
//     }
//     return 0;
// }
// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // arr_len은 배열 arr의 길이입니다.
// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* arr[], size_t arr_len) {
//     char*result = (char*)malloc(arr_len+1);
//     if(result == NULL){
//         return NULL;
//     }
    
//     for(size_t i = 0; i < arr_len; i++){
//         result[i] = arr[i][0];
//     }
    
//     result[arr_len] = '\0';
//     return result;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int a, int b) {
//     int temp = b;
//     int mul = 1;
    
//     while(temp > 0){
//         mul *= 10;
//         temp /= 10;
//     }
    
//     int result1 = a * mul + b;
//     int result2 = 2 * a * b;
    
//     if(result1 >= result2){
//         return result1;
//     }
//     else{
//         return result2;
//     }
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int* solution(int start_num, int end_num) {
//     int len = end_num - start_num + 1;
//     int* answer = (int*)malloc(sizeof(int) * len);
//     int start = start_num;
//     for(int i = 0; i < len; i++){
//         answer[i] = start;
//         start++;
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int n) {
//     int result = 0;
//     if(n % 2 != 0){
//         for(int i = 1; i <= n; i += 2){
//             result += i;
//         }
//     }
//     else{
//         for(int j = 2; j <= n; j += 2){
//             result += j * j;
//         }
//     }
//     return result;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int num, int n) {
//     int result = 0;
//     if(num % n == 0){
//         result = 1;
//     }
//     return result;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// int solution(int n, const char* control) {
//     int result = n;
//     for(int i = 0; control[i] != '\0'; i++){
//         if(control[i] == 'w'){
//             result += 1;
//         }
//         else if(control[i] == 's'){
//             result -= 1;
//         }
//         else if(control[i] == 'd'){
//             result += 10;
//         }
//         else if(control[i] == 'a'){
//             result -= 10;
//         }
//     }
//     return result;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // num_list_len은 배열 num_list의 길이입니다.
// int solution(int num_list[], size_t num_list_len) {
//     int result_mul = 1;
//     int result_add = 0;
//     int answer = 0;
//     for(size_t i = 0; i < num_list_len; i++){
//         result_mul *= num_list[i];
//         result_add += num_list[i];
//     }
//     result_add *= result_add;
//     if(result_mul < result_add){
//         answer = 1;
//     }
//     else{
//         answer = 0;
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(double flo) {
//     int floo = (int)flo;
//     return floo;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // num_list_len은 배열 num_list의 길이입니다.
// int* solution(int num_list[], size_t num_list_len, int n) {
//     int* answer = (int*)malloc(sizeof(int*) * n);
//     for(int i = 0; i < n; i++){
//         answer[i] = num_list[i];
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int a, int b, bool flag) {
//     int result = 0;
//     if(flag == true){
//         result = a + b;
//     }
//     else if(flag == false){
//         result = a - b;
//     }
//     return result;
// }

// #include <stdio.h>
// #define LEN_INPUT 11

// int main(void) {
//     char s1[LEN_INPUT];
//     scanf("%10s", s1);
    
//     for(int i = 0; s1[i] != '\0'; i++){
//         printf("%c\n", s1[i]);
//     }

//     return 0;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(const char* str1, const char* str2) {
//     for(int i = 0; str2[i] != '\0'; i++){
//         int j;
//         for(j = 0; str1[j] != '\0'; j++){
//             if(str2[i+j] != str1[j]){
//                 break;
//             }
//         }
//         if(str1[j] == '\0'){
//             return 1;
//         }
//     }
//     return 0;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// char* solution(const char* my_string, int index_list[], size_t index_list_len) {
//     // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
//     char* answer = (char*)malloc(sizeof(char) * (index_list_len + 1));
//     for(int i = 0; i < index_list_len; i++){
//         answer[i] = my_string[index_list[i]];
//     }
//     answer[index_list_len] = '\0';
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* my_string, int n) {
//     char* answer = (char*)malloc(sizeof(char) * (n+1));
//     for(int i = 0; i < n; i++){
//         answer[i] = my_string[i];
//     }
//     answer[n] = '\0';
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // num_list_len은 배열 num_list의 길이입니다.
// int* solution(int num_list[], size_t num_list_len) {
//     int* answer = (int*)malloc(sizeof(int) * (num_list_len + 1));
//     int n = num_list_len;
//     int last = num_list[n - 1];
//     int prev = num_list[n - 2];
//     int new;
//     if(last > prev){
//         new = last - prev;
//     }
//     else{
//         new = last * 2;
//     }
//     for(int i = 0; i < n+1; i++){
//         if(i == n){
//             answer[i] = new;
//             break;
//         }
//         answer[i] = num_list[i];
//     }
    
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>
// // str_list_len은 배열 str_list의 길이입니다.
// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* str_list[], size_t str_list_len, const char* ex) {
//     char* answer = (char*)malloc(sizeof(char) * 2001);
//     answer[0] = '\0';
    
//     for(int i = 0; i < str_list_len; i++){
//         if(strstr(str_list[i], ex) == NULL){
//             strcat(answer, str_list[i]);
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // arr_len은 배열 arr의 길이입니다.
// int* solution(int arr[], size_t arr_len){
//     int count = 0;
//     for(int i = 0; i < arr_len; i++){
//         count += arr[i];
//     }
//     int* answer = (int*)malloc(sizeof(int) * count);
//     int idx = 0;
//     for(int i = 0; i < arr_len; i++){
//         for(int j = 0; j < arr[i]; j++){
//             answer[idx++] = arr[i];
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // num_list_len은 배열 num_list의 길이입니다.
// int solution(int num_list[], size_t num_list_len) {
//     int answer = -1;
//     for(int i = 0; i < num_list_len; i++){
//         if(num_list[i] < 0){
//             return i;
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // arr_len은 배열 arr의 길이입니다.
// int* solution(int arr[], size_t arr_len, int k) {
//     int* answer = (int*)malloc(sizeof(int) * arr_len);
//     for(int i = 0; i < arr_len; i++){
//         if(k % 2 != 0){
//             answer[i] = arr[i] * k;
//         }
//         else{
//             answer[i] = arr[i] + k;
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// int solution(const char* my_string, const char* is_suffix) {
//     int my_len = strlen(my_string);
//     int suf_len = strlen(is_suffix);
    
//     if(suf_len > my_len){
//         return 0;
//     }
    
//     int start_idx = my_len - suf_len;
//     for(int i = 0; i < suf_len; i++){
//         if (my_string[start_idx + i] != is_suffix[i]) {
//             return 0;
//         }
//     }
//     return 1;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* myString) {
//     int len = strlen(myString);
//     char* answer = (char*)malloc(sizeof(char) *  (len + 1));
//     for(int i = 0; myString[i] != '\0'; i++){
//         if(myString[i] >= 97){
//             answer[i] = myString[i] - 32;
//         }
//         else{
//             answer[i] = myString[i];
//         }
//     }
//     answer[len] = '\0';
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int a, int b) {
//     int answer = 0;
//     if(a % 2 != 0 && b % 2 != 0){
//         answer = (a * a) + (b * b);
//     }
//     else if(a % 2 != 0 || b % 2 != 0){
//         answer = 2 * (a + b);
//     }
//     else if(a % 2 == 0 && b % 2 == 0){
//         if(a > b){
//             answer = a - b;
//         }
//         else{
//             answer = b - a;
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int num_list[], size_t num_list_len, int n) {
//     for(int i = 0; i < num_list_len; i++){
//         if(num_list[i] == n){
//             return 1;
//         }
//     }
//     return 0;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // arr_len은 배열 arr의 길이입니다.
// // delete_list_len은 배열 delete_list의 길이입니다.
// int* solution(int arr[], size_t arr_len, int delete_list[], size_t delete_list_len) {
//     int* answer = (int*)malloc(sizeof(int) * arr_len);
//     int idx = 0;
//     for(int i = 0; i < arr_len; i++){
//         int count = 0;
//         for(int j = 0; j < delete_list_len; j++){
//             if(arr[i] == delete_list[j]){
//                 count += 1;
//             }
//         }
//         if(count == 0){
//             answer[idx++] = arr[i]; 
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// char* solution(int n) {
//     char* answer = (char*)malloc(sizeof(char) * 12);
//     sprintf(answer, "%d", n);
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* n_str) {
//     int len = strlen(n_str);
//     int start = 0;
//     for(int i = 0; i < len; i++){
//         if(n_str[i] != '0'){
//             start = i;
//             break;
//         }
//     }
//     int new_len = len - start;
//     char* answer = (char*)malloc(sizeof(char) * (new_len+1));
//     for(int i = 0; i < new_len; i++){
//         answer[i] = n_str[start + i];
//     }
//     answer[new_len] = '\0';
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// int solution(const char* num_str) {
//     int answer = 0;
//     int len = strlen(num_str);
//     for(int i = 0; i < len; i++){
//         answer += (int)num_str[i] - '0';
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // num_list_len은 배열 num_list의 길이입니다.
// int* solution(int num_list[], size_t num_list_len) {
//     int* answer = (int*)malloc(sizeof(int) * (num_list_len - 5));
//     for(int i = 0; i < num_list_len - 1; i++){
//         for(int j = 0; j < num_list_len - i - 1; j++){
//             if (num_list[j] > num_list[j + 1]) {
//             int temp = num_list[j];
//             num_list[j] = num_list[j + 1];
//             num_list[j + 1] = temp;
//             }
//         }
//     }
//     for (int i = 5; i < num_list_len; i++) {
//         answer[i - 5] = num_list[i]; // answer[0]부터 차곡차곡 저장됨
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // arr_len은 배열 arr의 길이입니다.
// int* solution(int arr[], size_t arr_len, int n) {
//     int* answer = (int*)malloc(sizeof(int) * arr_len);
//     if(arr_len % 2 == 0){
//         for(int i = 0; i < arr_len; i++){
//             if(i % 2 != 0){
//                 answer[i] = arr[i] + n;
//             }
//             else{
//                 answer[i] = arr[i];
//             }
//         }
//     }
//     else{
//         for(int j = 0; j < arr_len; j++){
//             if(j % 2 == 0){
//                 answer[j] = arr[j] + n;
//             }
//             else{
//                 answer[j] = arr[j];
//             }
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* my_string, const char* alp) {
//     int len = strlen(my_string);
//     char* answer = (char*)malloc(sizeof(char) * (len+1));
//     for(int i = 0; i < len; i++){
//         if(my_string[i] == alp[0]){
//             answer[i] = my_string[i] - 32;
//         }
//         else{
//             answer[i] = my_string[i];
//         }
//     }
//     answer[len] = '\0';
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// long long solution(int a, int b) {
//     long long result = 0;
//     if(a > b){
//         for(int i = b; i <= a; i++){
//             result += i;
//         }
//     }
//     else{
//         for(int j = a; j <= b; j++){
//             result += j;
//         }
//     }
//     return result;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// int solution(const char* s) {
//     int answer = 0;
//     int buho = 1;
//     int start = 0;
//     if(s[0] == '+'){
//         start = 1;
//     }
//     else if(s[0] == '-'){
//         start = 1;
//         buho = -1;
//     }
//     for(int i = start; s[i] != '\0'; i++){
//         answer = answer * 10 + (s[i] - '0');
//     }
//     return answer * buho;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int n) {
//     int answer = 0;
//     for(int i = 1; i <= n; i++){
//         if(n % i == 0){
//             answer += i;
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int n) {
//     int answer = 0;
//     while(n > 0){
//         answer += n % 10;
//         n /= 10;
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int* solution(long long n) {
//     int idx = 0;
//     int* answer = (int*)malloc(sizeof(int) * 15);
//     while(n > 0){
//         answer[idx] = n % 10;
//         idx++;
//         n /= 10;
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// long long solution(long long n) {
//     long long answer = 0;
//     long long x = 1;
//     while(x * x < n){
//         x++;
//     }
//     if(x * x == n){
//         return (x+1) * (x+1);
//     }
//     else{
//         return -1;
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// char* solution(int num) {
//     if(num % 2 == 0){
//         return "Even";
//     }
//     else{
//         return "Odd";
//     }
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // arr_len은 배열 arr의 길이입니다.
// double solution(int arr[], size_t arr_len) {
//     double answer = 0;
//     for(int i = 0; i < arr_len; i++){
//         answer += arr[i];
//     }
//     answer /= arr_len;
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// bool solution(int x) {
//     bool answer = true;
//     int result = 0;
//     int temp = x;
//     while(temp > 0){
//         result += temp % 10;
//         temp /= 10;
//     }
//     if(x % result != 0){
//         answer = false;
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int n) {
//     int answer = 0;
//     for(int i = 1; i < n; i++){
//         if(n % i == 1){
//             answer = i;
//             break;
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // absolutes_len은 배열 absolutes의 길이입니다.
// // signs_len은 배열 signs의 길이입니다.
// int solution(int absolutes[], size_t absolutes_len, bool signs[], size_t signs_len) {
//     int answer = 0;
//     for(int i = 0; i < absolutes_len; i++){
//         if(signs[i] == true){
//             answer += absolutes[i];
//         }
//         else if(signs[i] == false){
//             answer += (absolutes[i] * -1);
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // numbers_len은 배열 numbers의 길이입니다.
// int solution(int numbers[], size_t numbers_len) {
//     int answer = 0;
//     for(int i = 0; i < 10; i++){
//         answer += i;
//     }
//     for(int j = 0; j < numbers_len; j++){
//         answer -= numbers[j];
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int num) {
//     long long n = num;
//     int count = 0;
//     while (n != 1) {
//         if (count == 500) {
//             return -1;
//         }
        
//         if (n % 2 == 0) {
//             n /= 2;
//         } else {
//             n = n * 3 + 1;
//         }
//         count++;
//     }
    
//     return count;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// char* solution(const char* phone_number) {
//     char* answer = (char*)malloc(sizeof(char) * 21);
//     int len = strlen(phone_number);
//     for(int i = 0; i < len; i++){
//         if(i < len - 4){
//             answer[i] = '*';
//         }
//         else{
//             answer[i] = phone_number[i];
//         }
//     }
//     answer[len] = '\0';
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// // a_len은 배열 a의 길이입니다.
// // b_len은 배열 b의 길이입니다.
// int solution(int a[], size_t a_len, int b[], size_t b_len) {
//     int answer = 0;
//     for(int i = 0; i < a_len; i++){
//         answer += a[i] * b[i];
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* s) {
//     char * answer;
//     int len = strlen(s);
//     if(len % 2 == 0){
//         answer = (char*)malloc(3);
//     }
//     else{
//         answer = (char*)malloc(2);
//     }
//     int idx = 0;
//     if(len % 2 != 0){
//         for(int i = 0; s[i] != '\0'; i++){
//             if(i == (len / 2)){
//                 answer[idx] = s[i];
//                 idx++;
//             }
//         }
//     }
//     else{
//         for(int j = 0; s[j] != '\0'; j++){
//             if(j == (len /2 -1) || j == (len /2)){
//                 answer[idx] = s[j];
//                 idx++;
//             }
//         }
//     }
//     answer[idx] = '\0';
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// char* solution(int n) {
//     char* answer = (char*)malloc(sizeof(char) * (n * 3) + 1);
//     answer[0] = '\0';
//     for(int i = 0; i < n; i++){
//         if(i % 2== 0){
//             strcat(answer, "수");
//         }
//         else{
//             strcat(answer, "박");
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// int solution(int left, int right) {
//     int answer = 0;
//     for(int i = left; i <= right; i++){
//         int count = 0;
//         for(int j = 1; j <= i; j++){
//             if(i % j == 0){
//                 count++;
//             }
//         }
//         if(count % 2 == 0){
//             answer += i;
//         }
//         else{
//             answer -= i;
//         }
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// char* solution(const char* s) {
//     int len = strlen(s);
//     char temp;
//     char* answer = (char*)malloc(sizeof(char) * (len+1));
//     strcpy(answer, s);
//     for(int i = 0; i < len - 1; i++){
//         for(int j = i + 1; j < len; j++){
//             if(answer[i] < answer[j]){
//                 temp = answer[i];
//                 answer[i] = answer[j];
//                 answer[j] = temp;
//             }
//         }
//     }
//     answer[len] = '\0';
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>

// long long solution(int price, int money, int count) {
//     long long answer = 0;
//     long long sum_price = 0;
//     for(int i = 1; i <= count; i++){
//         sum_price += (long long)price * i;
//     }
//     if(money < sum_price){
//         answer = sum_price - money;
//     }
//     else{
//         answer = 0;
//     }
//     return answer;
// }

// #include <stdio.h>
// #include <stdbool.h>
// #include <stdlib.h>
// #include <string.h>

// // 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
// bool solution(const char* s) {
//     int len = strlen(s);
//     bool answer = true;
//     if(len != 4 && len != 6){
//         return false;
//     }
//     for(int i = 0; i < len; i++){
//         if(s[i] < '0' || s[i] > '9'){
//             return false;
//         }
//     }
//     return answer;
// }

#include <stdio.h>

int main(void) {
    int a;
    int b;
    scanf("%d %d", &a, &b);
    for(int i = 0; i < b; i++){
        for(int j = 0; j < a; j++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}