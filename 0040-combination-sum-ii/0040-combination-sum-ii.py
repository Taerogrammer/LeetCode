class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        self.candidates = candidates
        candidates.sort()
        self.target = target
        self.ans = []
        
        self.backTracking(0, target, [])
        return self.ans

        
    def backTracking(self, prevIdx: int, cumSum: int, cur: list[int]):
        if cumSum == 0:
            self.ans.append(cur.copy())
            return
        elif cumSum < 0:
            return
        
        for i in range(prevIdx, len(self.candidates)):
            # 중복이거나 이미 확인한 인덱스는 continue
            if i > prevIdx and self.candidates[i-1] == self.candidates[i]:
                continue
            
            num = self.candidates[i]
            cur.append(num)
            self.backTracking(i+1, cumSum-num, cur)
            cur.pop()