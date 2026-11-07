#include <stdio.h>

int visited[100] = {0};

void initvisited(int n){
    for(int i = 0; i < n; i++){
        visited[i] = 0;
    }
}

void inittable(int n, int table[n][n]){
    for(int i = 0; i < n; i++){
        for(int j = 0; j < n; j++){
            table[i][j] = 0;
        }
    }
}

void dfs(int v, int n, int table[n][n]){
    visited[v] = 1;
    for(int i = 0; i < n; i++){
        if(visited[i] == 0 && table[v][i] == 1){
            dfs(i, n, table);
        }
    }
}

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    
    int table[n][n];
    inittable(n, table);

    for(int i = 0; i < m; i++){
        int s, e;
        scanf("%d %d", &s, &e);
        table[s][e] = 1;
        table[e][s] = 1;
    }

    int w1, w2;
    scanf("%d %d", &w1, &w2);

    initvisited(n);
    dfs(w1, n, table);
    if(visited[w1] && visited[w2]){
        printf("YES");
    }
    else{
        printf("NO");
    }
}