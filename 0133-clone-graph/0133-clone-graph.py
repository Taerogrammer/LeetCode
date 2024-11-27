"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
        
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # nul 가능성
        if not node:
            return
        
        tables = {}
        
        def dfs(node):
            # 주어진 노드가 해시 테이블의 키로 존재하면 해시 테이블에 저장되어있는 노드 반환하면서 해당 노드에 append 됨
            if node in tables:
                return tables[node]
            
            # 노드가 없다면 값을 복제 후 사용
            else:  
                value = Node(node.val)
                tables[node] = value
            
            # 이웃한 노드들을 추가한 뒤 반환
            for neighbor in node.neighbors:
                value.neighbors.append(dfs(neighbor))
            
            # 복제된 노드 반환
            return value
        
        return dfs(node)