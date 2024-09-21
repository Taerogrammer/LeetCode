class Solution:
    def addDigits(self, num: int) -> int:
        result = num
        
        while result > 9:
            digits = [int(digit) for digit in str(result)]
            result = 0
            for dig in digits:
                result += dig
        
        return result