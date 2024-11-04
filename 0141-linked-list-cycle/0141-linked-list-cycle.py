class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 토끼와 거북이 전략
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        hare, turtle = head, head
        
        # 토끼가 끝에 도달한다면, null이 나와서 False이지만,
        # 끝이 없다면 돌다가 언젠가 만나기 때문에 True
        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
            
            if turtle == hare:
                return True
        
        return False