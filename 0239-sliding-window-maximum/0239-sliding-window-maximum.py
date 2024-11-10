from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        queue = deque()
        
        # queue[0]: 최댓값의 인덱스
        for i in range(len(nums)):
            if queue and queue[0] < i - k + 1:  # 최댓값의 인덱스가 범위 벗어나면 pop
                queue.popleft()
            
            # 들어올 값(nums[i])보다 작은 값들은 pop후, nums[i]의 인덱스(i)를 큐에 추가
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            
            # 윈도우 크기가 k가 되었을 때부터 append
            if i >= k-1:
                ans.append(nums[queue[0]])
        
        return ans