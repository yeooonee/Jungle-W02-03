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

"""


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
    if visited is None:
        visited = []
    
    # 첫 정점
    visited.append(start)
    
    # 자식 노드 확인
    for i in graph[start]:  # [1,2]
        if i not in visited:
            # 자식 하나 잡자마자 자식 파고들기.
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
    
#     graph = {
#     1: [2, 3],
#     2: [4],
#     3: [5],
#     4: [],
#     5: []
# }
    
    print("=== DFS (깊이 우선 탐색) ===")
    result = dfs(graph, 1)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


