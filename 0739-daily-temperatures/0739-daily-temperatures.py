class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)
        
        for i, cur in enumerate(temperatures):
            # 스택이 비어있지 않고, 스택에 있는 값들이 현재값보다 작을 때까지 진행
            while stack and cur > temperatures[stack[-1]]:
               last = stack.pop()
               ans[last] = i - last
            stack.append(i)
        return ans