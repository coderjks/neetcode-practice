class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = dict()

        for string in strs:
            key = "".join(sorted(string))
            if key not in anagram_groups:
                anagram_groups[key] = list()
            anagram_groups[key].append(string)
        
        return [ group for group in anagram_groups.values()]