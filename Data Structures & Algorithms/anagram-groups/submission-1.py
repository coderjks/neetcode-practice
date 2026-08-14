class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = dict()

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagram_key = tuple(count)
            if anagram_key not in anagram_groups:
                anagram_groups[anagram_key] = list()
            anagram_groups[anagram_key].append(s)
        
        return list(anagram_groups.values())