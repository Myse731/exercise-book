#include <stdio.h>
void selectionSort(int arr[], int n){
    int countCompare = 0;
    int countSwap = 0;
    for(int i = 0; i < n - 1; i++){
        int minindex = i;
        for(int j = i + 1; j < n; j++){
            countCompare++;
            if(arr[j] < arr[minindex]){
                minindex = j;
            }
        }
        if(minindex != i){
            countSwap++;
            int temp = arr[i];
            arr[i] = arr[minindex];
            arr[minindex] = temp;
        }
    }
    printf("비교횟수 : %d, 교환 횟수 : %d\n", countCompare, countSwap);
}

void bubbleSort(int arr[], int n){
    int countCompare = 0;
    int countSwap = 0;
    for(int i = 0; i < n - 1; i++){
        int ct = 0;
        for(int j = 0; j < n - 1 - i; j++){
            countCompare++;
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                countSwap++;
                ct = 1;
            }
        }
        if(ct == 0){
            break;
        }
    }
    printf("비교횟수 : %d, 교환 횟수 : %d", countCompare, countSwap);
}

int main(){
    int arr[] = {4,1,7,3,8,2,6,5};
    int n = sizeof(arr) / sizeof(arr[0]);

    int arr2[] = {4,1,7,3,8,2,6,5};
    int n2 = sizeof(arr2) / sizeof(arr2[0]);

    selectionSort(arr, n);
    bubbleSort(arr2, n2);
}