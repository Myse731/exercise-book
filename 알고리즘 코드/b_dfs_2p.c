#include <stdio.h>

int visited[100][100] = {0};


void dfs(int a, int b, int n, int m, int map[n][m]){
    visited[a][b] = 1;

    int r[4] = {-1, 1, 0, 0};
    int c[4] = {0, 0, -1, 1};
    for(int i = 0; i < 4; i++){
        int nr = a + r[i];
        int nc = b + c[i];

        if(((0 <= nr && nr < n) && (0 <= nc && nc < m)) && map[nr][nc] == 1 && visited[nr][nc] == 0){
            dfs(nr, nc, n, m, map);
        }
    }
}

int main(){
    int n, m;
    scanf("%d %d", &n, &m);

    int map[n][m];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%d", &map[i][j]);
        }
    }

    printf("==Map==\n");
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            printf("%d ", map[i][j]);
        }
        printf("\n");
    }


    int count = 0;
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            if(map[i][j] == 1 && visited[i][j] == 0){
                count++;
                dfs(i, j,  n, m, map);
            }
        }
    }
    printf("섬 : %d", count);
}