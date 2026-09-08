"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque


# 이중배열 첫 요소 비교 
# while 문 안에서 for i,j in edges:  # 왜 i 가 [] 로 나오는지?
# i 가 [] 로 나오는 이유 

# 큐에 넣고 나오면서 차수 빼기
# 1. 그래프 형태 정의 [정점, 진입차수] 및 정점 기준으로 초기화
# 2. 간선으로 진입 차수 추가 
# 3. 진입 차수가 0인 정점들을 큐에 추가 
# 4. 큐 반복하기
# 4-1. 큐에서 정점 꺼내기
# 4-2. pop 한 정점 == edges 시작 정점일 때, graph의 차수 조회하여 큐에 없으면 (정점, 차수) 형태로 큐에 저장
# 4-3. 현재 꺼낸 값에 차수가 있으면 차수 감소 & 다시 큐에 추가, 없으면 결과 추가 

# -> (0,1)(1,2)(2,3) 케이스 커버 못해서 수정

# 차수가 0인 것만 큐에 넣기
# 1. 그래프 형태 정의 [정점, 진입차수] 및 정점 기준으로 초기화
# 2. 간선으로 진입 차수 추가 
# 3. 진입 차수가 0인 정점들을 큐에 추가 
# 4. 큐 반복하기 & 결과값 추가 
# 4-1. 큐에서 정점 꺼내기
# 4-2. 큐와 인접한 정점 차수 조회 후 0보다 크면 빼기, 0이면 큐에 추가

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    # (정점, 진입차수) 형태
    graph = [[i,0] for i in range(vertices)]
    # graph = []
    queue = deque() # deque 의 기본값 []


    # TODO: 그래프 구성 및 진입 차수 계산
    for i,j in edges:
        if j == graph[j][0]:
            graph[j][1] += 1
    
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    for i in graph:     # [정점, 차수] 형태
        if i[1] == 0: 
            queue.append(i)
    
    result = []
    
    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소
    while queue:
        # 큐에서 정점 꺼내기 
        v = queue.popleft()
        result.append(v[0])
        
        # # 인접한 정점 큐에 추가하기 
        # for i,j in edges:   # 왜 i 가 [] 로 나오는지?
        #     # pop 한 정점이랑 edges의 시작 정점이랑 같을 때 
        #     if v[0] == i:
        #         # graph 의 차수 조회
        #         for a in graph:
        #             # graph 의 정점 [0] 과 edges 의 [1]이 같을 때 그 차수 조회해오기 (전체 graph)
        #             # 인접한 정점(j)이 간선 출발점(i)이 아닐때
        #             if a[0] == j and i != a[0]:
        #             # 정점 가지고 graph 조회해오기
        #                 # val = graph[j]
        #                 queue.append(a) 
                
        # 인접한 정점 큐에 추가하기 
        for i, j in edges: # i: 간선 출발점, j : 간선 도착점
            if v[0] == i:   # v[0]: queue 꺼낸 값의 정점 
                for a in graph: # 차수 조회
                    if a[0] == j : # 그래프의 정점이랑 같을때
                        if a[1] > 0: # 차수가 0보다 크면
                            a[1] -= 1   # 감소
                        if a[1] == 0:
                            queue.append(a)
        
        
                            
                
        # 현재 꺼낸 값 차수가 있으면 차수 감소 & 다시 큐에 추가, 없으면 결과 추가
        # if v[1] > 0 :
        #     v[1] -= 1
        #     # 큐에 다시 추가 
        #     queue.append(v)
        #     continue
        # elif v[1] == 0:
        #     result.append(v[0])
    
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")
