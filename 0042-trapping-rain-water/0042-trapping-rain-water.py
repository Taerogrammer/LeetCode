class Solution:
    def trap(self, height: list[int]) -> int:
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        volumes = 0
        
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            
            # 왼쪽의 높이가 더 작으면 이동 및 부피 추가
            if l_max <= r_max:
                volumes += l_max - height[l]
                l += 1
            else:
                volumes += r_max - height[r]
                r -= 1
        
        return volumes