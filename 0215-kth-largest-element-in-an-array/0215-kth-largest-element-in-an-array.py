import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # 최소힙으로 만들기
        heapq.heapify(nums)
        
        for i in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)


        ## 처음 풀이
        heap = list()
        
        # 최대 힙으로 삽입
        for num in nums:
            heapq.heappush(heap, -num)
        # k-1번째까지 pop
        for i in range(k-1):
            heapq.heappop(heap)
        
        # k번째 pop
        return -heapq.heappop(heap)
