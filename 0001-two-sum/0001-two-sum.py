class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original = list(enumerate(nums))
        
        original.sort(key=lambda x: x[1])
        
        (l, r) = (0, len(original)-1)
        
        while l < r:
            if original[l][1] + original[r][1] == target:
                return [original[l][0], original[r][0]]
            elif original[l][1] + original[r][1] > target:
                r -= 1
            else:
                l += 1