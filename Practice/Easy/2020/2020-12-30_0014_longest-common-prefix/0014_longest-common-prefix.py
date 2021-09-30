class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        common = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for word in strs:
                if len(word) <= i or word[i] != c:
                    return common
            common += c
        return common
