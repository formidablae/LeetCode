class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer = 0
        for i in range(1, len(points)):
            previous = points[i - 1]
            actual = points[i]
            if previous[0] == actual[0]:
                answer += abs(actual[1] - previous[1])
            elif previous[1] == actual[1]:
                answer += abs(actual[0] - previous[0])
            else:
                diag = min(abs(previous[0] - actual[0]), abs(previous[1] - actual[1]))
                horiz = abs(previous[0] - actual[0]) - diag
                verti = abs(previous[1] - actual[1]) - diag
                answer += diag + horiz + verti
        return answer
