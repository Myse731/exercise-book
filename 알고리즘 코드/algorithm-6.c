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
    int min = arr[1] - arr[0];
    int minIndex = 0;
    for(int i = 0; i < n-1; i++){
        if((arr[i+1] - arr[i]) < min){
            min = arr[i+1] - arr[i];
            minIndex = i;
        }
    }
    return minIndex;
}

int main(){
    int n;
    scanf("%d", &n);
    int numbers[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &numbers[i]);
    }
    CheckSearch(numbers, n);
    int minIndex = printArr(numbers, n);
    printf("%d %d", numbers[minIndex], numbers[minIndex+1]);
}