/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public var val: Int
 *     public var left: TreeNode?
 *     public var right: TreeNode?
 *     public init() { self.val = 0; self.left = nil; self.right = nil; }
 *     public init(_ val: Int) { self.val = val; self.left = nil; self.right = nil; }
 *     public init(_ val: Int, _ left: TreeNode?, _ right: TreeNode?) {
 *         self.val = val
 *         self.left = left
 *         self.right = right
 *     }
 * }
 */



class Solution {
    func findTarget(_ root: TreeNode?, _ k: Int) -> Bool {
        var set = Set<Int>()
        return findValue(root,k, &set)
    }
    
    private func findValue(_ node: TreeNode?, _ k: Int, _ set: inout Set<Int>) -> Bool {
        guard let node = node else {
            return false
        }
        
        if set.contains(k - node.val) {
            return true
        }
        
        set.insert(node.val)
        
        return findValue(node.left, k, &set) || findValue(node.right, k, &set)
    }
}