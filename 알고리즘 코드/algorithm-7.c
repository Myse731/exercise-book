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

void Checking(int arr1[], int n, int arr2[], int m, int result[]){
    for(int i = 0; i < m; i++){
        for(int j = 0; j < n; j++){
            if(arr2[i] == arr1[j]){
                result[i] = 1;
            }
        }
    }
}

int main(){
    int n;
    scanf("%d", &n);
    int number1[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &number1[i]);
    }
    CheckSearch(number1, n);

    int m;
    scanf("%d", &m);
    int number2[m];
    for(int i = 0; i < m; i++){
        scanf("%d", &number2[i]);
    }

    int result[m];
    for(int i = 0; i < m; i++){
        result[i] = 0;
    }
    
    Checking(number1, n, number2, m, result);
    for(int i = 0; i < m; i++){
        printf("%d ", result[i]);
    }
}