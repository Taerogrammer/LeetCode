class Solution {
    func answerQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let n = nums.count, m = queries.count, sortNums = nums.sorted()
        var left = 0, right = n - 1, sum = 0, cnt = 0, result = [Int]()
        
        for i in 0..<m {
            for j in 0..<n {
                if sum + sortNums[j] <= queries[i] {
                    sum += sortNums[j]
                    cnt += 1
                }
            }
            result.append(cnt)
            sum = 0
            cnt = 0
        }        
        return result
    }
}