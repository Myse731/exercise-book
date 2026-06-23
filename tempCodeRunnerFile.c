int main(void){
    int arr[5];
    for(int i = 0; i < 5; i++){
        scanf("%d", &arr[i]);
    }
    for(int j = 0; j < 4; j++){
        for(int u = 0; u < 4 - j; u++){
            if(arr[u] >= arr[u+1]){
                swap(&arr[u], &arr[u+1]);
            }
        }
    }
    for(int i = 0; i < 5; i++){
        printf("%d", arr[i]);
    }
}