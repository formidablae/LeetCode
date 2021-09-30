class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            flag = True
            for c in word:
                if c not in allowed:
                    flag = False
                    break
            if flag:
                count += 1
        return count
