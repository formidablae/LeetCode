class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        self = self
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        dim = len(s)
        a = s[0:dim//2]
        b = s[dim//2: dim]
        count_a = 0
        count_b = 0
        for i in range(dim//2):
            if a[i] in vowels:
                count_a += 1
            if b[i] in vowels:
                count_b += 1
        return count_a == count_b


sl = Solution()
tc_1_str = "book"
print(sl.halvesAreAlike(tc_1_str))
print()
tc_2_str = "textbook"
print(sl.halvesAreAlike(tc_2_str))
print()
tc_3_str = "MerryChristmas"
print(sl.halvesAreAlike(tc_3_str))
print()
tc_4_str = "AbCdEfGh"
print(sl.halvesAreAlike(tc_4_str))
print()