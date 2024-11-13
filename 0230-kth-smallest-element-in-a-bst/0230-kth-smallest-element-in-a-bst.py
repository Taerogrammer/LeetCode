# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        cnt = 0
        
        while stack or node:
            while node: # left를 탐방
                stack.append(node)
                node = node.left
                
            # cnt +1 하면서 만약 인덱스가 있다면 해당 node의 값을 반환
            cnt += 1
            node = stack.pop()
            if cnt == k:
                return node.val
        
            # 이래도 없다면 right 탐색
            node = node.right