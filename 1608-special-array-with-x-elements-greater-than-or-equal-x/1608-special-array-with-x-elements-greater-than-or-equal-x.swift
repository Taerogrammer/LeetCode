/**
1. x값과 정렬된 배열을 지정한다.
2. mid를 기준으로 나눈다.
3. count = mid를 기준으로 배열에서 조건을 만족하는 값의 개수
4. 
*/

class Solution {
    func specialArray(_ nums: [Int]) -> Int {
        let x = nums.count, array = nums.sorted()
        var left = 0, right = x - 1
        
        while left <= right {
            let mid = left + (right - left) / 2
            let count = x - mid
            
            if array[mid] >= count {
                if mid == 0 || array[mid - 1] < count {
                    return count
                } else {
                    right = mid - 1
                }
            } else {
                left = mid + 1
            }
        }
        
        return -1
    }
}