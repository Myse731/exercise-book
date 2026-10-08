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

void Checking(int arr1[], int arr2[], int n, int m){
    int i = 0;
    int j = 0;
    int count = 0;
    while(i < n && j < m){
        if(arr1[i] == arr2[j]){
            printf("%d ", arr1[i]);
            i += 1;
            j += 1;
            count++;
        }
        else if(arr1[i] < arr2[j]){
            i += 1;
        }
        else{
            j += 1;
        }
    }
    if(count == 0){
        printf("-1");
    }
}

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    int number1[n];
    int number2[m];

    for(int i = 0; i < n; i++){
        scanf("%d", &number1[i]);
    }
    CheckSearch(number1, n);
    for(int j = 0; j < m; j++){
        scanf("%d", &number2[j]);
    }
    CheckSearch(number2, m);

    Checking(number1, number2, n, m);
}