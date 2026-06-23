// #include <stdio.h>

// int chars(char * arr){
//     int sum = 0;
//     while(*(arr++) != '\0'){
//         sum += 1;
//     }

//     return sum;
// }

// void pal(char * arr){
//     char arr2[11];

//     int len = chars(arr);

//     for(int i = 0; i < len; i++){
//         *(arr2 + len -1 -i) = *(arr + i);
//     }

//     arr2[len] = '\0';

//     int same = 1;

//     for(int i = 0; i < len; i++){
//         if(*(arr2 + i) == *(arr + i)){
//             same = 0;
//             break;
//         }
//     }

//     if(same == 1){
//         printf("palindrome");
//     }
//     else{
//         printf("not palindrome");
//     }
// }


// int main(void){
//     char arr[11];

//     scanf("%10s", arr);

//     pal(arr);
// }

//1번
// #include <stdio.h>

// int main() {
//     int arr[5] = {1, 2};

//     for (int i = 0; i < 5; i++) {
//         printf("%d ", arr[i]);
//     }

//     return 0;
// }
//1, 2, 쓰레기 값, 쓰레기 값, 쓰레기 값 -> 0으로 초기화


//2번
// int arr[4];
// 1000, 1004, 1008, 1012

//3번
// char str[] = "ABC";
// 4byte

//4번
// #include <stdio.h>

// int main() {
//     int a = 10;
//     int *p = &a;

//     *p = 30;

//     printf("%d\n", a);

//     return 0;
// }
// 30

//5번
// #include <stdio.h>

// int main() {
//     int arr[3] = {10, 20, 30};
//     int *p = arr;

//     printf("%d\n", *(p + 1));

//     return 0;
// }
// 20 

//6번
// int arr[2][3] = {
//     {1, 2, 3},
//     {4, 5, 6}
// };
// 1 ~ 6이 일렬로 저장됨

//7번
// A. int *arr[5];
// B. int (*arr)[5];
// B번 -> A번

//8번
// #include <stdio.h>
// int main(void){
//     int arr[3] = {1, 2, 3};
//     arr++;
//     printf("%d", &arr);
// }
// 상수라서 바꿀수 없음 -> 포인터 변수가 아니라서 증감연산이 되지 않는다.

//9번
// char *str = "hello";
// str[0] = 'H';
// 읽기전용이라서 할수 없다. -> 잘못된 접근입니다.

//10번
// #include <stdio.h>
// #include <stdlib.h>

// int main() {
//     int n = 5;
//     int *arr = malloc(n * sizeof(int));

//     if (arr == NULL) {
//         return 1;
//     }

//     // 메모리 해제
//     ___________;

//     return 0;
// } -> free(arr);

// #include <stdio.h>
// int main(void){
// 	printf("Hello\n");
// 	printf("World");
// 	return 0;
// }

// #include <stdio.h>
// int main(void){
// 	printf(" \'Hello World\" ");
// }

// #include <stdio.h>
// int main(void){
// 	long long a;
// 	double b;
// 	char c;
// 	scanf("%lld %lf %c", &a,&b,&c);
// 	printf("%lld %.10lf %c", a, b, c);
// 	return 0;
// }

// #include <stdio.h>
// #include <stdbool.h>
// int main() {
// 	int a, b;
// 	scanf("%d %d", &a, &b);
// 	printf("%d\n%d\n%d", a&&b, a||b, !a);
// 	return 0;
// }

#include <stdio.h>
int main(void){
    char arr[101];
    fgets(arr, 100, stdin);
    for(int i = 0; arr[i] != '\0' ; i++){
        if(*(arr+i) != ' '){
            printf("%c", *(arr+i));
        }
    }
}