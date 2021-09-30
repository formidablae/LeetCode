class Solution:
    def maximumUnits(self, boxTypes: list, truckSize: int) -> int:
        self = self
        sorted_boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        filled = 0
        count = 0
        for i in range(len(sorted_boxTypes)):
            if sorted_boxTypes[i][0] == truckSize - count:
                filled += sorted_boxTypes[i][0] * sorted_boxTypes[i][1]
                count += sorted_boxTypes[i][0]
                break
            elif sorted_boxTypes[i][0] < truckSize - count:
                filled += sorted_boxTypes[i][0] * sorted_boxTypes[i][1]
                count += sorted_boxTypes[i][0]
            else:
                how_many = truckSize - count
                filled += how_many * sorted_boxTypes[i][1]
                count += how_many
            # print("filled", filled,
            #       "count", count,
            #       "box[0]", sorted_boxTypes[i][0],
            #       "box[1]", sorted_boxTypes[i][1],
            #       "box[0] * box[1]", sorted_boxTypes[i][0] * sorted_boxTypes[i][1])
        return filled


sl = Solution()
tc_1_lst = [[1, 3], [2, 2], [3, 1]]
tc_1_int = 4
tc_2_lst = [[5, 10], [2, 5], [4, 7], [3, 9]]
tc_2_int = 10
print("Expected  8, got", sl.maximumUnits(tc_1_lst, tc_1_int))
print("Expected 91, got", sl.maximumUnits(tc_2_lst, tc_2_int))
