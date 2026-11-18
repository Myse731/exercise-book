#include <stdio.h>

#define INF 999999
#define N 6

int graph[N][N] = {
    {0, 2, 4, INF, INF, INF},
    {2, 0, 3, 3, INF, INF},
    {4, 3, 0, 2, INF, INF},
    {INF, 3, 2, 0, 5, 8},
    {INF, INF, INF, 5, 0, 4},
    {INF, INF, INF, 8, 4, 0},
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
        if(u == -1) break;
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
    char *places[N] = {"부산역", "초량 이바구길", "영도 흰여울 문화마을", "남포동 비프마을", "감천문화마을", "광안리 해수욕장"};
    
    printf("출발 장소: %s\n\n", places[start]);
    for(int i = 0; i < N; i++){
        if(dist[i] == INF){
            printf("%s : INF\n",  places[i]);
        }
        else{
            printf("%s : %d분\n", places[i], dist[i] * 10);
        }
    }
}