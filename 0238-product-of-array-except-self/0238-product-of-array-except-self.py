class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left, leftTmp = [1], 1
        right, rightTmp = [1], 1
        ans = []
        
        for i in range(1, len(nums)):
            leftTmp *= nums[i-1]
            left.append(leftTmp)
            rightTmp *= nums[len(nums)-i]
            right.append(rightTmp)
            
        right.reverse()
        
        for i in range(len(nums)):
            ans.append(left[i] * right[i])
        
        return ans