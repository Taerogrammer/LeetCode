class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans = []
        intervals.sort(key=lambda x:(x[0]))
        left, right = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):
            if right >= intervals[i][0]:
                right = max(right, intervals[i][1])
            else:
                ans.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]
        ans.append([left, right])   #   마지막 추가
        
        return ans