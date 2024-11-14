class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        array = []
        l, r, idx = 0, 0, 0
        mid = (m+n) // 2
        
        while True:
            # 배열을 다 탐색했다면 최댓값 넣기
            v1 = nums1[l] if l < m else 1000001
            v2 = nums2[r] if r < n else 1000001
            # 왼쪽 값이 작으면 왼쪽값 대입, 반대 동일
            if v1 <= v2:
                array.append(v1)
                l += 1
            else:
                array.append(v2)
                r += 1
            
            # 중앙 도달
            if idx == mid:
                # 짝수
                if (m + n) % 2 == 0:
                    return (array[-2] + array[-1]) / 2
                else:
                    return array[-1]
            
            idx += 1