#include <stdio.h>

// 큐로 사용할 배열 (N, M이 최대 100일 때 넉넉하게 잡는 것이 좋음)
int q_r[10000], q_c[10000];
int front = 0, rear = 0;

// 방문 여부 및 이동 거리를 저장할 배열 (-1: 미방문)
int visited[100][100];

// visited 배열을 전부 -1로 초기화 (아직 방문 안 함을 표시)
void initvisit(void){
    for(int i = 0; i < 100; i++){
        for(int j = 0; j < 100; j++){
            visited[i][j] = -1;
        }
    }
}

void bfs(int n, int m, int map[n][m]){
    // 출발점(0, 0) 초기화: 시작 지점 거리는 0
    visited[0][0] = 0;
    
    // 시작 위치 큐에 push
    q_r[rear] = 0;
    q_c[rear] = 0;
    rear++;

    // 큐가 빌 때까지 반복 (BFS)
    while(front < rear){
        // 큐에서 현재 위치 pop
        int r = q_r[front];
        int c = q_c[front];
        front++;

        // 상, 하, 좌, 우 이동용 델타 배열
        int mr[4] = {-1, 1, 0, 0};
        int mc[4] = {0, 0, -1, 1};

        // 4방향 탐색
        for(int i = 0; i < 4; i++){
            int nr = r + mr[i];
            int nc = c + mc[i];

            // 1. 맵 범위 안에 있고
            // 2. 아직 방문하지 않았고 (-1)
            // 3. 이동 가능한 칸(0)인 경우
            if(((0 <= nr && nr < n) && (0 <= nc && nc < m)) && visited[nr][nc] == -1 && map[nr][nc] == 0){
                // 다음 칸 거리 = 현재 칸 거리 + 1
                visited[nr][nc] = visited[r][c] + 1;

                // 다음 위치 큐에 push
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
    
    // N x M 크기의 미로 입력
    int map[n][m];
    for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
            scanf("%d", &map[i][j]);
        }
    }
    
    // 방문 배열 초기화
    initvisit();

    // BFS 탐색 시작
    bfs(n, m, map);
    
    // 목적지(N-1, M-1)까지의 최소 이동 횟수 출력
    // [리뷰 메모]: 자동 채점 사이트 제출 시에는 "최소 이동 횟수 : " 문구를 빼고 %d만 출력해야 맞음!
    printf("최소 이동 횟수 : %d", visited[n-1][m-1]);
    
    return 0;
}