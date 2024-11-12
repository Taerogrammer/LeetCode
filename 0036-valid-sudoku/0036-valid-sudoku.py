class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows, cols, boxes = [set() for _ in range(9)], [set() for _ in range(9)], [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                num = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)
                
                if num in rows[r]:
                    return False
                if num in cols[c]:
                    return False
                if num in boxes[box_index]:
                    return False
                
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_index].add(num)
        
        return True
                