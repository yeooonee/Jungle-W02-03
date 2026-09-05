"""
[DFS - 깊이 우선 탐색 (Depth-First Search)]

문제 설명:
- DFS로 그래프를 탐색합니다.
- 깊이 방향으로 끝까지 탐색합니다.
- 재귀 또는 스택을 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
DFS: [0, 1, 2, 3] (순서는 구현에 따라 다를 수 있음)

힌트:
- 재귀로 구현
- 방문 체크 필요
- 깊이 우선으로 방문
"""


# 스택으로 구현했을 때는 [0,2,3,1] 로 결과가 예상됨
# 순서가 안 중요한 경우 (그래프가 연결되어있는지, 몇 개의 컴포넌트로 나뉘는지, 특정 노드에 도달 가능한지)
# 순서가 중요한 경우 (방문 순서를 출력하라, 어떤 경로로 갔다가 되돌아왔는지, 사전순으로 가장 빠른 경로 찾기, 방문 순서에 따라 결과가 달라지는 계산)
def dfs(graph, start, visited=None):
    """
    깊이 우선 탐색 (재귀)
    
    Args:
        graph: 그래프 딕셔너리
        start: 현재 정점
        visited: 방문 리스트
    
    Returns:
        방문 순서 리스트
    """
    # TODO: visited가 None이면 초기화 [재귀 호출에서 비어있을 때 최초로 초기화 필요]
    if visited is None:
        visited = []
    
    # TODO: 현재 정점 방문
    visited.append(start)
    
    # TODO: 인접한 정점들에 대해 재귀
    ## 방문하지 않은 정점이면 재귀 호출
    # 모든 정점 반복문
    
    # [시작정점의 연결점 확인]
    for i in graph[start]:
        # [연결점이 방문하지 않았을 때]
        if i not in visited:
            # [재귀호출]
            dfs(graph, i, visited)
    
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


