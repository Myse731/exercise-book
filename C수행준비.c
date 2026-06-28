// #include <stdio.h>
// int main(void){
//     char arr[101];
//     int sum = 0;
//     fgets(arr, 100, stdin);
//     for(int i = 0; *(arr+i) != '\0'; i++){
//         if(*(arr+i) != ' '){
//             printf("%c", *(arr+i));
//         }
//     }
// }

// #include <stdio.h>
// void swap(int *a,int *b){
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }
// int main(void){
//     int a, b;
//     scanf("%d %d", &a, &b);
//     printf("a : %d, b :  %d\n", a, b);
//     swap(&a, &b);
//     printf("a : %d, b :  %d", a, b);
// }

// #include <stdio.h>
// void swap(int *a,int *b){
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }

// #include <stdio.h>
// void swap(int * a, int * b){
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }
// int main(void){
//     int arr[5];
//     for(int i = 0; i < 5; i++){
//         scanf("%d", &arr[i]);
//     }
//     for(int j = 0; j < 4; j++){
//         for(int u = 0; u < 4 - j; u++){
//             if(arr[u] >= arr[u+1]){
//                 swap(&arr[u], &arr[u+1]);
//             }
//         }
//     }
//     for(int i = 0; i < 5; i++){
//         printf("%d ", arr[i]);
//     }
// }

// #include <stdio.h>
// int main(void){
//     int age;
//     char moon;
//     scanf("%d", &age);
//     scanf(" %c", &moon);
//     printf("나이 : %d, 학과 : %c", age, moon);
// }

// #include <stdio.h>
// void visitor_count(){
//     static int a;
//     a += 1;
//     printf("%d번째 방문입니다.\n", a);
// }

// int main(void){
//     visitor_count();
//     visitor_count();
//     visitor_count();
//     visitor_count();
// }

// #include <stdio.h>
// int chars(char * arr){
//     int sum = 0;
//     for(int h = 0; *(arr+h) != '\0'; h++){
//         sum += 1;
//     }
//     return sum;
// }

// int main(void){
//     char arr[101];
//     scanf("%s", arr);
//     for(int i = 0; arr[i] != '\0'; i++){
//         printf("%c", *(arr+i));
//     }
//     printf("\n");
//     int len = chars(arr);
//     for(int j = len - 1; j >= 0; j--){
//         printf("%c", *(arr+j));
//     }
// }

// #include <stdio.h>
// int max(int * arr){
//     int max = arr[0], max_idx = 0;
//     for(int j = 0; j < 5; j++){
//         if(arr[j] >= max){
//             max = arr[j];
//             max_idx = j;
//         }
//     }
//     return max_idx;
// }

// int min(int * arr){
//     int min = arr[0], min_idx = 0;
//     for(int h = 0; h < 5; h++){
//         if(arr[h] <= min){
//             min = arr[h];
//             min_idx = h;
//         }
//     }
//     return min_idx;
// }
// int main(void){
//     int arr[5];
//     for(int i= 0; i < 5; i++){
//         scanf("%d", &arr[i]);
//     }
//     printf("%d ", max(arr) + 1);
//     printf("%d", min(arr) + 1);
// }

// #include <stdio.h>
// int main(void){
//     int n;
//     scanf("%d", &n);
//     int arr[n];
//     for(int i = 0; i < n; i++){
//         scanf("%d", &arr[i]);
//     }
//     for(int j = 0; j < n; j++){
//         printf("%d : ", j+1);
//         for(int h = 0; h < n; h++){
//             if(j == h){
//                 continue;
//             }
//             if(arr[j] < arr[h]){
//                 printf("< ");
//             }
//             else if(arr[j] > arr[h]){
//                 printf("> ");
//             }
//             else{
//                 printf("= ");
//             }
//         }
//         printf("\n");
//     }
// }

// #include <stdio.h>
// int main(void){
//     int n;
//     scanf("%d", &n);
//     int arr[n];
//     for(int i = 0; i < n; i++){
//         scanf("%d", &arr[i]);
//     }
//     for(int j = 0; j < n; j++){
//         for(int h = j; h < n; h++){
//             printf("%d ", arr[h]);
//         }
//         for(int g = 0; g < j; g++){
//             printf("%d ", arr[g]);
//         }
//         printf("\n");
//     }
// }

// #include <stdio.h>
// int main(void){
//     int arr[10];
//     for(int i = 0; i < 10; i++){
//         scanf("%d", &arr[i]);
//     }
//     int k;
//     scanf("%d", &k);
//     for(int j = 0; j < 10; j++){
//         if(j == k-1){
//             printf("%d", arr[j]);
//         }
//     }
// }

// #include <stdio.h>
// int main(void){
//     char arr[100000];
//     scanf("%s", arr);
//     int sum1 = 0;
//     int sum2 = 0;
//     for(int i = 0; arr[i] != '\0'; i++){
//         if(arr[i] == '('){
//             sum1++;
//         }
//         else if(arr[i] == ')'){
//             sum2++;
//         }
//     }
//     printf("%d %d", sum1, sum2);
// }

// #include <stdio.h>
// int main(void){
//     int n;
//     int add = 1;
//     scanf("%d", &n);
//     int arr[n][n];
//     for(int i = 0; i < n; i++){
//         if(i % 2== 0){
//             for(int j = 0; j < n; j++){
//                 arr[i][j] = add++;
//             }
//         }
//         else if(i % 2 != 0){
//             for(int h = n - 1; h >= 0; h--){
//                 arr[i][h] = add++;
//             }
//         }
//     }
//     for(int f = 0; f < n; f++){
//         for(int d = 0; d < n; d++){
//             printf("%d ", arr[f][d]);
//         }
//         printf("\n");
//     }
// }

// #include <stdio.h>
// int main(void){
//     int n, m;
//     int add = 1;
//     scanf("%d %d", &n, &m);
//     int arr[n][m];
//     for(int i = 0; i < m; i++){
//         for(int j = 0; j < n; j++){
//             arr[j][i] = add++;
//         }
//     }
//      for(int i = 0; i < n; i++){
//         for(int j = 0; j < m; j++){
//             printf("%d ", arr[i][j]);
//         }
//         printf("\n");
//     }
// }

// #include <stdio.h>
// int main(void){
//     int add = 1;
//     int arr[3][3];
//     for(int i = 0; i < 3; i++){
//         for(int j = 0; j < 3; j++){
//             arr[i][j] = add++;
//         }
//     }
//     for(int i = 0; i < 3; i++){
//         int sum = 0;
//         for(int j = 0; j < 3; j++){
//             sum += arr[i][j];
//         }
//         printf("%d ", sum);
//     }
// }

// #include <stdio.h>
// int main(void){
//     char arr[101];
//     fgets(arr, 100, stdin);
//     for(int i = 0; arr[i] != '\0'; i++){
//         if(arr[i] != ' '){
//             printf("%c", arr[i]);
//         }
//     }
// }