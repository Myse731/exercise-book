#include <stdio.h>

#define V 5

int graph[V][V] ={
    {0, 1, 1, 0, 1},
    {1, 0, 0, 1, 0},
    {1, 0, 0, 1, 1},
    {0, 1, 1, 0, 0},
    {1, 0, 1, 0, 0}
};

void printGraph(){
    printf("  ");
    for(int i = 0; i < V; i++){
        printf("%d ", i);
    }
    printf("\n");
    for(int i = 0; i < V; i++){
        printf("%d ", i);
        for(int j = 0; j < V; j++){
            printf("%d ", graph[i][j]);
        }
        printf("\n");
    }
}

int visited[V];

void initvisited(void){
    for(int i = 0; i < V; i++){
        visited[i] = 0;
    }
}

void dfs(int v){
    visited[v] = 1;
    printf("%d ", v);
    for(int i = 0; i < V; i++){
        if(visited[i] == 0 && graph[v][i] == 1){
            dfs(i);
        }
    }
}

void bfs(int start){
    int queue[V];
    int front = 0;
    int rear = 0;

    visited[start] = 1;
    queue[rear++] = start;
    while(front < rear){
        int v = queue[front++];
        printf("%d ", v);
        for(int i = 0; i < V; i++){
            if(graph[v][i] && !visited[i]){
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main(void){
    printf("[인접행렬]\n");
    printGraph();

    printf("\n[DFS 탐색 순서]\n");
    dfs(0);
    printf("\n");

    initvisited();
    
    printf("\n[BFS 탐색 순서]\n");
    bfs(0);
    printf("\n");
    return 0;
}