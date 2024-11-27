class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        self.candidates = candidates
        self.target = target
        self.ans = []
        
        self.backTracking(0, target, [])
        return self.ans
        
    def backTracking(self, prevIdx: int, cumSum: int, ans:list[int]):
        if cumSum == 0:
            self.ans.append(ans.copy())
            return
        elif cumSum < 0:
            return

        for idx in range(prevIdx, len(self.candidates)):
            num = self.candidates[idx]
            
            # 재귀
            ans.append(num)
            self.backTracking(idx, cumSum-num, ans)
            # 다 돌고 난 후 pop
            ans.pop()