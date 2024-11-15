import heapq

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        
        # 첫 번째 열의 요소들을 추가하고, (값, 행 인덱스, 열 인덱스)를 저장합니다.
        for i in range(n):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))
        for _ in range(k - 1):
            # 최솟값, 해당 값의 행, 열을 추출
            val, row, col = heapq.heappop(min_heap)
            # 다음 열의 요소를 추가합니다(범위를 벗어나지 않는 경우).
            if col + 1 < n:
                heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))        
        
        return heapq.heappop(min_heap)[0]
    
# sort: O(n log n)
# heap: O(k log n)