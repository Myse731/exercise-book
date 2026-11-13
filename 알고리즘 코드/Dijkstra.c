#include <stdio.h>

#define INF 999999
#define N 6

int graph[N][N] = {
    {0, 7, 4, 9, INF, INF},
    {7, 0, INF, 2, 6, INF},
    {4, INF, 0, 3, INF, 8},
    {9, 2, 3, 0, 4, INF},
    {INF, 6, INF, 4, 0, 2},
    {INF, INF, 8, INF, 2, 0},
};

int dist[N];
int visited[N];

int findMinVertex(int dist[N], int visited[N]){
    int min = INF;
    int minIndex = -1;

    for(int i = 0; i < N; i++){
        if(min > dist[i] && visited[i] == 0){
            min = dist[i];
            minIndex = i;
        }
    }
    return minIndex;
}

void Dijkstra(int start){
    for(int i = 0; i < N; i++){
        dist[i] = INF;
        visited[i] = 0;
    }
    dist[start] = 0;
    for(int count = 0; count < N; count++){
        int u = findMinVertex(dist, visited);
            visited[u] = 1;
            for(int v = 0; v < N; v++){
                if(graph[u][v] != INF && visited[v] == 0){
                    if(dist[u] + graph[u][v] < dist[v]){
                        dist[v] = dist[u] + graph[u][v];
                    }
                }
            }
        }
    }

int main(){
    int start = 0;
    Dijkstra(start);
    printf("시작 정점 %d번으로부터 각 정점까지의 최단 거리:\n", start);
    for (int i = 0; i < N; i++) {
        if (dist[i] == INF) {
            printf("정점 %d : 도달 불가\n", i);
        } else {
            printf("정점 %d : %d\n", i, dist[i]);
        }
    }
}