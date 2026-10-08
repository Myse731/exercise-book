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

int binarySearch(int arr[], int n, int target) {
    int low = 0;
    int high = n - 1;

    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[mid] == target) {
            return 1; 
        } else if (arr[mid] > target) {
            high = mid - 1; 
        } else {
            low = mid + 1;  
        }
    }

    return 0;
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

    for(int i = 0; i < m; i++){
        printf("%d ", binarySearch(number1, n, number2[i]));
    }
    printf("\n");

    return 0;
}