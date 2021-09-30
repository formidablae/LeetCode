class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        dim = len(s)
        a = s[0:dim//2]
        b = s[dim//2: dim]
        print(a)
        print(b)
        count_a = 0
        count_b = 0
        for i in range(dim//2):
            if a[i] in vowels:
                count_a += 1
            if b[i] in vowels:
                count_b += 1
        return count_a == count_b
