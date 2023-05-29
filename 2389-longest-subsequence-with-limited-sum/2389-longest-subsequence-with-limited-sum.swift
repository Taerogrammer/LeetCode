class Solution {
    func answerQueries(_ nums: [Int], _ queries: [Int]) -> [Int] {
        let n = nums.count, m = queries.count, sortNums = nums.sorted()
        var result = [Int]()
        
        for i in 0..<m {
            var cnt = 0
            var sum = 0
            
            while cnt < n && (sortNums[cnt] + sum) <= queries[i] {
                sum += sortNums[cnt]
                cnt += 1
            }
            result.append(cnt)
        }
        return result
    }
}