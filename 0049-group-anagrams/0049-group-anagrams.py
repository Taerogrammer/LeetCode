class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 딕셔너리
        anagrams = {}
        
        for s in strs:
            key = tuple(sorted(s))
            
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(s)
        
        return list(anagrams.values())