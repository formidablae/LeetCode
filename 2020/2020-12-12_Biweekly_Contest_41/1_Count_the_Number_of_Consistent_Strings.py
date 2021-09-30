class Solution:
    def countConsistentStrings(allowed, words) -> int:
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

    allowed = "abc"
    words = ["a","b","c","ab","ac","bc","abc"]
    print(countConsistentStrings(allowed, words))