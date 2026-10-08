#include <stdio.h>
#include <stdlib.h>
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

int printArr(int arr[], int n, int target){
    int minIndex = 0;
    int min = abs(target - arr[0]);
    for(int i = 0; i < n; i++){
        if(abs(target - arr[i]) < min){
            min = abs(target - arr[i]);
            minIndex = i;
        }
    }
    return minIndex;
}

int main(){
    int n, k;
    scanf("%d %d", &n, &k);
    int numbers[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &numbers[i]);
    }
    CheckSearch(numbers, n);
    int minIndex = printArr(numbers, n, k);
    printf("%d", numbers[minIndex]);
}