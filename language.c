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

// #include <stdio.h>
// int main() {
// 	double a, b;
// 	scanf("%lf%lf", &a, &b);
// 	swap(&a, &b);
// 	printf("%.2f %.2f", a, b);
// 	return 0;
// }
// void swap(double *a, double *b){
// 	double temp = *a;
// 	*a = *b;
// 	*b = temp;
// }

// #include <stdio.h>
// void sort(int *a, int *b, int *c)
// {
//     if (*a > *b)
//     {
//         swap(a, b);
//     }
//     if (*a > *c)
//     {
//         swap(a, c);
//     }
//     if (*b > *c)
//     {
//         swap(b, c);
//     }
// }
// void swap(int *a, int *b)
// {
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }
// int main() {
// 	int a, b, c;
// 	scanf("%d%d%d", &a, &b, &c);
// 	sort(&a, &b, &c);
// 	printf("%d %d %d", a, b, c);
// }

// #include <stdio.h>
// int main()
// {
//     int arr[5], i;
//     for (i = 0; i < 5; i++)
//     {
//         scanf("%d", arr + i);
//     }
//     printf("%d", max(arr));
// }
// int max(int *arr)
// {
//     int max = 0;
//     for (int j = 0; j < 5; j++)
//     {
//         if (max <= *(arr + j))
//         {
//             max = *(arr + j);
//         }
//     }
//     return max;
// }

// #include <stdio.h>
// #include <stdlib.h>

// int max(int *, int);
// int main()
// {
//     int n;
//     scanf("%d", &n);
//     int j;
//     int *arr = (int *)malloc(sizeof(int) * n);

//     for (j = 0; j < n; j++)
//     {
//         scanf("%d", arr + j);
//     }

//     printf("%d", max(arr, n));
// }
// int max(int *arr, int n)
// {
//     int max = 0;
//     for (int h = 0; h < n; h++)
//     {
//         if (max <= *(arr + h))
//         {
//             max = *(arr + h);
//         }
//     }
//     return max;
// }

// #include <stdio.h>
// int main()
// {
//     char arr[11];
//     scanf("%s", arr);
//     printf("%d", chars(arr));
// }
// int chars(char *arr)
// {
//     int sum = 0;
//     while (*(arr++) != '\0')
//     {
//         sum += 1;
//     }
//     return sum;
// }

// #include <stdio.h>

// int chars(char * arr){
//    int sum = 0;

//    while(*(arr++) != '\0'){
//        sum += 1;
//    }

//    return sum;
// }

// void pal(char *arr){

//     char arr2[11];

//     int len = chars(arr);

//     for(int i = 0; i < len; i++){
//         *(arr2 + len - i - 1) = *(arr + i);
//     }

//     arr2[len] = '\0';

//     int same = 1;

//     for(int i = 0; i < len; i++){
//         if(*(arr2 + i) != *(arr + i)){
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

// #include <stdio.h>
// void swap(int *a, int *b){
// 	int temp = *a;
// 	*a = *b;
// 	*b = temp;
// }

// int min(int * arr,int start, int n){
// 	int idx = start;
// 	for(int i = start; i < n; i++){
// 		if(*(arr + idx) >= *(arr + i)){
// 			idx = i;
// 		}
// 	}
// 	return idx;
// }


// int main(void){
// 	int n;
// 	scanf("%d", &n);
// 	int arr[n];
// 	for(int i = 0; i < n; i++){
// 		scanf("%d", arr + i);
// 	}
// 	for(int i = 0; i < n-1; i++){
// 		swap(arr+i, arr+min(arr, i, n));
// 	}
// 	for(int i = 0; i < n; i++){
// 		printf("%d ", *(arr + i));
// 	}
// }