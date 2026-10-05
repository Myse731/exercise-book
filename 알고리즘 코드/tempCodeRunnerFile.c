#include <stdio.h>
int scoreSearch(int arr[], int n, int score){
    int low = 0;
    int high = n - 1;
    int result = -1;

    while(low <= high){
        int mid = (low+high)/2;
        if(arr[mid] >= score){
            result = mid + 1;
            high = mid -1;
        }
        else if(arr[mid] < score){
            low = mid + 1;
        }
    }
    return result;
}

int main(){
    int n = 0;
    int score = 0;

    scanf("%d %d", &n, &score);
    int numbers[n];
    for(int i = 0; i < n; i++){
        scanf("%d", &numbers[i]);
    }

    int result = scoreSearch(numbers, n, score);
    printf("%d", result);
}