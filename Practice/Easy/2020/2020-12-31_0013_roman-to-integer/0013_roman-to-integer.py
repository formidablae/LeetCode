class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1,
                  "V": 5,
                  "X": 10,
                  "L": 50,
                  "C": 100,
                  "D": 500,
                  "M": 1000}
        reducers = "IXC"
        composed = {"IV": 4,
                    "IX": 9,
                    "XL": 40,
                    "XC": 90,
                    "CD": 400,
                    "CM": 900}
        integ = 0
        i = 0
        while i < len(s) - 1:
            c = s[i]
            if c in reducers:
                cc = s[i: i + 2]
                if cc in composed.keys():
                    integ += composed[cc]
                    i += 2
                else:
                    integ += values[c]
                    i += 1
            else:
                integ += values[c]
                i += 1
        if i == len(s) - 1:
            integ += values[s[i]]
        return integ
                
