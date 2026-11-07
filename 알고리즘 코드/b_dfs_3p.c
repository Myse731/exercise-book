#include <stdio.h>
int q_r[10000], q_c[10000];
int front = 0, rear = 0;

int visited[100][100];

void initvisit(void){
    for(int i = 0; i < 100; i++){
        for(int j = 0; j < 100; j++){
            visited[i][j] = -1;
        }
    }
}

void bfs(int n, int m, int map[n][m]){
    visited[0][0] = 0;
    q_r[rear] = 0;
    q_c[rear] = 0;
    rear++;

    while(front < rear){
        int r = q_r[front];
        int c = q_c[front];
        front++;

        int mr[4] = {-1, 1, 0, 0};
        int mc[4] = {0, 0, -1, 1};

        for(int i = 0; i < 4; i++){
            int nr = r + mr[i];
            int nc = c + mc[i];

            if(((0 <= nr && nr < n) && (0 <= nc && nc < m)) && visited[nr][nc] == -1 && map[nr][nc] == 0){
                visited[nr][nc] = visited[r][c] + 1;

                q_r[rear] = nr;
                q_c[rear] = nc;

                rear++;
            }
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
            printf("%d ",map[i][j]);
        }
        printf("\n");
    }

    initvisit();

    bfs(n, m, map);
    printf("최소 이동 횟수 : %d", visited[n-1][m-1]);
}