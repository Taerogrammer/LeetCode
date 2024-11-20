class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        left, right, merged = [], [], newInterval
        
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left += interval,
            elif interval[0] > newInterval[1]:
                right += interval,
            else:
                merged[0] = min(interval[0], merged[0])
                merged[1] = max(interval[1], merged[1])
        
        return left + [merged] + right