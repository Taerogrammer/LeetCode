class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        # 0 : not visited, 1 : visiting, 2 : visited
        visited = [0] * numCourses
        
        for a, b in prerequisites:
                graph[a].append(b)
        
        def dfs(node):
            # 만약 방문 중인데 또 방문하면 false
            if visited[node] == 1:
                return False
            # 이미 방문했으면 true 반환하고 계속 탐색
            elif visited[node] == 2:
                return True
            
            # 방문 시작
            visited[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False

            # visiting이 완료되면 visited로 변환
            visited[node] = 2
            return True
        
        for i in range(numCourses):
            # 방문하지 않은 노드에 대해 dfs에서 false가 나왔다면
            if visited[i] == 0 and not dfs(i):
                return False
        
        return True