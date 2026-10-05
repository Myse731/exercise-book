#include <stdio.h>
void CheckSearch(int arr[], int n){
    for(int i = 0; i < n-1; i++){
        int minIndex = i;
        for(int j = i+1; j < n; j++){
            if(arr[j] > arr[minIndex]){
                minIndex = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}

int main(){
    int n = 0;
    int k = 0;

    scanf("%d %d", &n, &k);
    int numbers[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &numbers[i]);
    }
    CheckSearch(numbers, n);
    printf("%d", numbers[k-1]);
}