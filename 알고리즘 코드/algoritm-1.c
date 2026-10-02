#include <stdio.h>
int linerSearch(int arr[], int size, int target){
    for(int i = 0; i < size; i++){
        if(arr[i] == target){
            return i+1;
        }
    }
    return -1;
}


int main(){
    int n;
    scanf("%d", &n);
    int numbers[n];
    for(int i = 0; i < n; i++){
        int number = 0;
        scanf("%d", &number);
        numbers[i] = number;
    }
    int target = 0;
    scanf("%d", &target);

    int size = sizeof(numbers) / sizeof(numbers[0]);
    int result = linerSearch(numbers, size, target);
    if(result == -1){
        printf("찾지 못했습니다 : -1");
    }
    else{
        printf("%d번째에 출석번호 %d 위치", result, numbers[result-1]);
    }
}