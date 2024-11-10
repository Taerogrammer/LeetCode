class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # idx: 순회 인덱스, red: 0, blue: 2
        idx, red, blue = 0, 0, len(nums)-1
        
        while idx <= blue:
            if nums[idx] == 0:
                nums[idx], nums[red] = nums[red], nums[idx] # swap
                red += 1
                idx += 1
            elif nums[idx] == 2:
                nums[idx], nums[blue] = nums[blue], nums[idx]
                blue -= 1
            else:
                idx += 1
                
        return nums