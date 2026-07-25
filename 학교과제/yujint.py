# 학교 기숙사 인터넷망 최소 비용 구축9크루스칼)
# 정점 v와 간선 e 입력받기
v, e = map(int, input().split())

# 간선리스트와 인접리스트 생성
edges = []
graph = [[] for i in range(v)]

# 간선 정보 입력 받기
for i in range(e):
    a, b, cost = map(int, input().split())

    # 무방향 그래프 이기에 양쪽에 저장
    graph[a].append((b, cost))
    graph[b].append((a, cost))

    # 간선 리스트에 저장
    edges.append((cost, a, b))

# 비용에 따라 정렬
edges.sort()

# 부모 초기화
parent = list(range(v))

# 부모 찾기
def find(x):
    if parent[x] == x:
        return x
    return find(parent[x])

#최소 신장 트리 생성, 합계 초기화
mst = []
total = 0

# 크루스칼
for cost, a, b in edges:
    # 서로 다른 집합인지 확인
    if find(a) != find(b):
        # 다르면 연결
        parent[find(b)] = find(a)
        # 최소 신장 트리에 저장
        mst.append((a, b, cost))
        # 합계에 값 더하기
        total += cost
    # 정점이 모두 연결 되면 종료
    if len(mst) == v - 1:
        break
# 출력 결과
print('선택된 연결 경로')
for a, b, cost in mst:
    print(f"{a} - {b} : {cost}")
print(f'총 최소 설치 비용 : {total}')