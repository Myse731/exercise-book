#include <stdio.h>
int linearSearch(int arr[], int size, int target){
    for(int i = 0; i < size; i++){
        if(arr[i] == target){
            return i;
        }
    }
    return -1;
}
int main(void){
    int arr[] = {13, 8, 27, 4, 19};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target;

    printf("찾을 숫자 입력: ");
    scanf("%d", &target);

    int result = linearSearch(arr, size, target);

    if(result == -1){
        printf("%d는 배열에 없습니다\n", target);
    }
    else{
        printf("%d는 %d번째 인덱스에서 찾았습니다.", target, result);
    }
    return 0;
}