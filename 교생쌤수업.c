// 함수 활용
// #include <stdio.h>
// void swap(int *a, int *b){
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }
// int main(void){
//     int x = 10;
//     int y = 20;
//     swap(&x, &y);
//     printf("%d %d", x, y);
// }

//포인터 : 변수의 주소를 가지고 있는 변수
// #include <stdio.h>
// int main(void){
//     int number = 10;
//     int *p;
//     p = &number;
//     printf("%d", *p);
// }

// p를 출력하면 변수의 주소값이 나오고, *p는 변수의 값이 나온다.(* 간접 참조 연산자)

// #include <stdio.h>
// int main(void){
//     int a = 10;
//     int *p;
//     p = &a;

//     *p = 30;
//     printf("%d %d", *p, a);
//     return 0;
// }

// #include <stdio.h>
// int main(void){
//     char *pc;
//     int *pi;
//     double *pd;

//     pc = (char *)10000;
//     pi = (int *)10000;
//     pd = (double *)10000;
//     printf("증가전 pc = %d, pi  = %d, pd = %d\n", pc, pi, pd);

//     pc++;
//     pd++;
//     pi++;
//     printf("증가후 pc = %d, pi  = %d, pd = %d\n", pc, pi, pd);
// }

// v = *p++ p가 가리키는 값을 v에 대입한 후에 p 증가
// v = (*p)++ p가 가리키는 값을 v에 대입한 후에 가리키는 값증가

// #include <stdio.h>
// int main(void){
//     int a = 10;
//     int *p;
//     p = &a;
//     printf("%d\n",(*p)++);
//     printf("%d\n",++*p);
//     printf("%d\n",*p++);
//     printf("%d\n",a);
//     printf("%d\n",*++p);
// }

// void modify(int *ptr){
//     *ptr = 99;
// }

// int main(){
//     int num = 1;
//     modify(&num);
//     printf("num = %d", num);
//     return 0;
// }

//포인터 사용시 유의점 : 포인터 P가 초기화 안됨, 포인터가 가리키는게 무엇인지도 모르는데 가리키는 값을 건드림
//포인터의 타입 == 변수의 타입