class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aList = list(map(int, a))
        bList = list(map(int, b))
        aList.reverse()
        bList.reverse()
        (aValue, bValue) = (0, 0)
        for i in range(len(aList)):
            aValue += aList[i] * pow(2, i)
        for i in range(len(bList)):
            bValue += bList[i] * pow(2, i)
            
        return bin(aValue+bValue)[2:]
    # 다른 풀이 (format)
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), 'b')
