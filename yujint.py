# 학교 급식실 식재료 배송망 최소 비용 구축 프로그램
# 크루스칼 알고리즘을 이용하여 모든 창고와 급식실을
# 최소 운송 비용으로 연결하는 최소 신장 트리(MST)를 구한다.

# 배송 경로 정보를 저장할 리스트
edges = []

# 정점(창고 및 급식실)의 개수와 간선(배송 경로)의 개수 입력
n, m = map(int, input().split())

# 배송 경로 정보 입력
# u: 출발 정점, v: 도착 정점, cost: 운송 비용
for _ in range(m):
    u, v, cost = map(int, input().split())
    edges.append((u, v, cost))

# 운송 비용이 낮은 경로부터 선택하기 위해 비용 기준으로 정렬
edges.sort(key=lambda x: x[2])

# 각 정점의 부모를 자기 자신으로 초기화
parent = [i for i in range(n)]

# 정점이 속한 집합의 대표(부모) 노드를 찾는 함수
def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

# 서로 다른 두 집합을 하나의 집합으로 합치는 함수
def union(parent, a, b):
    root_a = find(parent, a)
    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a

# 크루스칼 알고리즘을 수행하는 함수
def kruskal(edges):

    # 최소 총 운송 비용
    total_cost = 0

    # 최소 신장 트리에 포함된 배송 경로 저장
    mst = []

    # 비용이 가장 작은 경로부터 확인
    for u, v, cost in edges:

        # 두 정점이 다른 집합에 속해 있다면
        # 사이클이 발생하지 않으므로 선택
        if find(parent, u) != find(parent, v):

            # 선택된 배송 경로 저장
            mst.append((u, v, cost))

            # 총 운송 비용 누적
            total_cost += cost

            # 두 정점을 같은 집합으로 연결
            union(parent, u, v)

        # 정점이 모두 연결되면 종료
        if len(mst) == n - 1:
            break

    return mst, total_cost

# 크루스칼 알고리즘 실행
mst, total_cost = kruskal(edges)

# 결과 출력
print("선택된 경로")
for u, v, cost in mst:
    print(f"{u} - {v} : {cost}")

print(f"최소 총 운송 비용 : {total_cost}")