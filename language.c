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

// #include <stdio.h>
// int main(void){
//     char arr[101];
//     fgets(arr, 100, stdin);
//     for(int i = 0; arr[i] != '\0' ; i++){
//         if(*(arr+i) != ' '){
//             printf("%c", *(arr+i));
//         }
//     }
// }

// #include <stdio.h>
// int main(void){
// 	int n;
// 	scanf("%d", &n);
// 	int called[24] = {0};
// 	int count[24] = {0};
// 	for(int i = 0; i < n; i++){
// 		scanf("%d", &called[i]);
// 	}
// 	for(int j = 0; j < n; j++){
// 		int number = called[j];
//         if (number != 0) {
// 		count[number - 1] += 1;
//         }
// 	}
// 	for(int h = 0; h < 23; h++){
// 		printf("%d ", count[h]);
// 	}
// }

// #include <stdio.h>
// int main(void){
// 	int n;
//     scanf("%d", &n);
//     int arr[n];
//     for(int i = 0; i < n; i++){
//         scanf("%d", &arr[i]);
//     }
//     for(int j = 0; j < n; j++){
//         printf("%d\n", arr[j]);
//     }
//     for(int j = 0; j < n; j++){
//         printf("%d\n", arr[j]);
//     }
// }

// #include <stdio.h>
// int main(void){
//     int n;
//     scanf("%d", &n);
//     int arr[n];
//     for(int u = 0; u < n; u++){
//         scanf("%d", &arr[u]);
//     }
//     for(int i = 0; i < n; i++){
//         for(int j = i; j < n; j++){
//             printf("%d", arr[j]);
//         }
//         for(int h = 0; h < i; h++){
//             printf("%d", arr[h]);
//         }
//         printf("\n");
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

// #include <stdio.h>
// int main(void){
//     int n;
//     scanf("%d", &n);
//     char name[n];
//     int score[n];
//     for(int i = 0; i< n; i++){
//         scanf("%s %d", name, score);
//     }
//     for(int j = 0; j < 3; j++){
//         int max = 0, maxidx = 0;
//         for(int h = 0; h < n; h++){
//             if(max <= score[h]){
//                 max = score[h];
//                 maxidx = h;
//             }
//         }
//         score[maxidx] = 0;
//         printf("%s", name[maxidx]);
//     }
   
// }


// #include <stdio.h>
// int main(void){
// 	int n;
// 	scanf("%d", &n);
// 	int arr[n];
// 	for(int i = 0; i < n; i++){
// 		scanf("%d", &arr[i]);
// 	}
// 	for(int i = n - 1; i >= 0; i--){
// 		printf("%d ", arr[i]);
// 	}
// }

// #include <stdio.h>
// int main(void){
// 	int n;
// 	scanf("%d", &n);
// 	int arr[n];
// 	for(int i = 0; i < n; i++){
// 		scanf("%d", &arr[i]);
// 	}
// 	for(int j = 0; j < n; j++){
// 		for(int k = j; k < n; k++){
// 			printf("%d ", arr[k]);
// 		}
// 		for(int h = 0; h < j; h++){
// 			printf("%d ", arr[h]);
// 		}
//         printf("\n");
// 	}
// }

// #include <stdio.h>
// int main(void){
// 	char arr[101];
// 	fgets(arr, sizeof(arr), stdin);
// 	for(int i = 0; arr[i] != '\0'; i++){
// 		if(arr[i] != ' '){
// 			printf("%c", arr[i]);
// 		}
// 	}
// }

// #include <stdio.h>
// int main(void){
// 	char a[100000];
// 	scanf("%s", a);
// 	int sumr = 0, suml = 0;
// 	for(int i = 0; a[i] != '\0'; i++){
// 		if(a[i] == '('){
// 			suml += 1;
// 		}
// 		else if(a[i] == ')'){
// 			sumr += 1;
// 		}
// 	}
// 	printf("%d %d", suml, sumr);
// }

// #include <stdio.h>
// int main(void){
// 	int n;
// 	scanf("%d", &n);
// 	int cards[n-1];
// 	int sum1 = 0;
// 	int sum2 = 0;
// 	for(int i = 0; i < n - 1; i++){
// 		scanf("%d", &cards[i]);
// 	}
// 	for(int j = 0; j < n - 1; j++){
// 		sum1 += cards[j];
// 	}
// 	for(int k = 1; k < n+1; k++){
// 		sum2 += k;
// 	}
// 	int sum3 = sum2 - sum1;
// 	printf("%d", sum3);
// }

// #include <stdio.h>
// int main(void){
// 	int n;
// 	scanf("%d", &n);
// 	int arr[1000];
// 	for(int i = 0; i < n; i++){
// 		scanf("%d", &arr[i]);
// 	}
// 	for(int j = 0; j < n; j++){
//         printf("%d: ", j+1);
// 		for(int k = 0; k < n; k++){
// 			if(k == j){
// 				continue;
// 			}
// 			if(arr[j] > arr[k]){
// 				printf("> ");
// 			}
// 			else if(arr[j] < arr[k]){
// 				printf("< ");
// 			}
// 			else if(arr[j] == arr[k]){
// 				printf("= ");
// 			}
// 		}
//         printf("\n");
// 	}
// }

// #include <stdio.h>
// int main(void){
// 	char arr[100];
// 	scanf("%s", arr);
// 	for(int i = 0; arr[i] != '\0'; i++){
// 		if(arr[i] >= 65 && arr[i] <= 90){
// 			arr[i] += 32;
// 		}
// 		else if(arr[i] >= 97 && arr[i] <= 122){
// 			arr[i] -= 32;
// 		}
// 	}
// 	printf("%s", arr);
// }

// #include <stdio.h>
// int main(void){
// 	char word[16];
// 	scanf("%s", word);
// 	if(word == 'love'){
// 		printf("I Love you");
// 	}
// 	else{
// 		printf("");
// 	}
// }

// #include <stdio.h>
// int main(void){
// 	int n;
// 	int add = 1;
// 	scanf("%d", &n);
// 	int arr[n][n];
// 	for(int i = 0; i < n; i++){
// 		for(int j = 0; j < n; j++){
// 			arr[i][j] = add++;
// 		}
// 	}
// 	for(int k = 0; k < n; k++){
// 		for(int h = 0; h < n; h++){
// 			printf("%d ", arr[k][h]);
// 		}
// 		printf("\n");
// 	}
// }

// #include <stdio.h>
// int main(void){
// 	int n;
// 	scanf("%d", &n);
// 	int add = 1;
// 	int arr[100][100];
// 	for(int i = 0; i < n; i++){
// 		if(i % 2 == 0){
// 			for(int j = 0; j < n; j++){
// 				arr[i][j] = add++;
// 			}
// 		}

// 		else{
// 			for(int j = n - 1; j >= 0; j--){
// 				arr[i][j] = add++;
// 			}
// 		}
// 	}
// 	for(int i = 0; i < n; i++){
// 		for(int j = 0; j < n; j++){
// 			printf("%d ", arr[i][j]);
// 		}
// 		printf("\n");
// 	}
// }

// #include <stdio.h>
// int main(void){
// 	int n;
// 	scanf("%d", &n);
//     int arr[n];
//     for(int i = 0; i < n; i++){
//         scanf("%d", &arr[i]);
//     }
//     int sums[n];
//     int sum = 0;
//     for(int j = 0; j < n; j++){
//         sum += arr[j];
//         sums[j] = sum;
//     }
//     for(int k = 0; k < n; k++){
//         printf("%d ", sums[k]);
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
//     int step[n/2];
//     int add = 0;
//     for(int j = 0; j < n; j += 2){
//         if(arr[j] >= arr[j+1]){
//             step[add++] =  arr[j];
//         }
//         else{
//             step[add++] = arr[j+1];
//         }
//     }
//     for(int k = 0; k < n / 2; k++){
//         printf("%d ", step[k]);
//     }
// }

// #include <stdio.h>
// int main(void){
//     int n;
//     scanf("%d", &n);
//     int arr[n][n];
//     int add = 1;
//     for(int i = 0; i < n; i++){
//         for(int j = n - 1; j >= 0; j--){
//             arr[i][j] = add++;
//         }
//     }
//     for(int i = 0; i < n; i++){
//         for(int j = 0; j < n; j++){
//             printf("%d ", arr[i][j]);
//         }
//         printf("\n");
//     }
// }

// #include <stdio.h>
// int main(void){
//     int n,m;
//     scanf("%d %d", &n, &m);
//     int arr[n][m];
//     int add = 1;
//     for(int i = m - 1; i >= 0; i--){
//         for(int j = 0; j < n; j++){
//             arr[j][i] = add++;
//         }
//     }
//     for(int i = 0; i < n; i++){
//         for(int j = 0; j < m; j++){
//             printf("%d ", arr[i][j]);
//         }
//         printf("\n");
//     }
// }

// #include <stdio.h>
// int main(void){
//     int n;
//     scanf("%d", &n);
//     int arr[n][n];
//     int add = 1;
//     for(int i = 0; i < n; i++){
//         for(int j = 0; j < n; j++){

//         }
//     }
// }

// #include <stdio.h>
// int main(void){
// 	char words[9];
// 	scanf("%s", words);
// 	printf("%s", words);
// }

// #include <stdio.h>
// int main(void){
// 	char words[51];
// 	fgets(words, 51, stdin);
// 	int count = 0;
// 	for(int i = 0; words[i] != '\0'; i++){
// 		if((words[i] >= 'A' && words[i] <= 'Z') || (words[i] >= 'a' && words[i] <= 'z')){
// 			continue;
// 		}
// 		count += 1;
// 	}
// 	printf("%d", count);
// }


// #include <stdio.h>

// int odd_sum(int n);

// int main() {
// 	int n, i;
// 	scanf("%d", &n);
// 	printf("%d", odd_sum(n));
// }

// int odd_sum(int n){
// 	int sum = 0;
// 	if(n == 1){
// 		return 1;
// 	}
// 	else if(n % 2 != 0){
// 		return n + odd_sum(n-1);
// 	}
// 	return odd_sum(n-1);
// }

#include <stdio.h>
#include <stdlib.h>
void print_array(int **arr, int n) {
	int i, j;
	for(i = 0; i < n; i++) {
		for(j = 0; j < n; j++) {
			printf("%5d", arr[i][j]);
		}
		printf("\n");
	}	
}
int main() {
int n;
scanf("%d", &n);
int **arr = (int**)malloc(sizeof(int *) * n);
for(int i = 0; i < n; i++){
	arr[i] = (int *)malloc(sizeof(int) * n);
}

int add = 1;
for(int i = 0; i < n; i++){
	if(i % 2 != 0){
		for(int j = n - 1; j >= 0; j--){
			arr[j][i] = add++;
		}
	}
	else{
		for(int j = 0; j < n; j++){
			arr[j][i] = add++;
		}
	}
}
	print_array(arr, n);
}