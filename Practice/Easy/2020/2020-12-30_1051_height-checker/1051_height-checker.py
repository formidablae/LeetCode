class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        target = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != target[i]:
                count += 1
        return count
