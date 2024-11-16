class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest = 0
        
        for num in nums:
            # 첫 번째 자리가 아니면 찾을 필요가 없음 (포함됨) -> 결국 배열(nums)을 한 번씩 순회하는 것이기 때문에 O(1)로 나와 O(n)의 시간 복잡도를 가짐
            if num - 1 in nums_set:
                continue
            length = 1
            while num + length in nums_set:
                length += 1
            longest = max(longest, length)
        
        return longest