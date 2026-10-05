#include <stdio.h>
void CheckSearch(int arr[], int n){
    for(int i = 0; i < n-1; i++){
        int minIndex = i;
        for(int j = i+1; j < n; j++){
            if(arr[j] < arr[minIndex]){
                minIndex = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

int printArr(int arr[], int n){
    for(int i = 0; i < n; i++){
        if(i > 0){
            if(arr[i] != arr[i-1]){
                printf("%d ", arr[i]);
            }
        }
        else{
            printf("%d ", arr[i]);
        }
    }
}

int main(){
    int n;
    scanf("%d", &n);
    int numbers[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &numbers[i]);
    }
    CheckSearch(numbers, n);
    printArr(numbers, n);
}