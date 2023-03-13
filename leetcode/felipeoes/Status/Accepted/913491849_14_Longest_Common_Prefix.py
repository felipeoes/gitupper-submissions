class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixes = {}
        
        for word in strs:
            for i in range(len(word)):
                prefixes[word[:i+1]] = prefixes.get(word[:i+1], 0) + 1
                
        max_prefix = ""
        for prefix in prefixes:
            if prefixes[prefix] == len(strs) and len(prefix) > len(max_prefix):
                max_prefix = prefix
                
        return max_prefix
