import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 최소힙으로 만들기
        heapq.heapify(nums)
        
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)