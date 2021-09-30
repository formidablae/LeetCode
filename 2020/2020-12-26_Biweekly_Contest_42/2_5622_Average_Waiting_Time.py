class Solution:
    def method(self, customers: list) -> float:
        self = self
        preparation_times = [customers[0][0] + customers[0][1]]
        wait_times = [customers[0][1]]
        # print("preparation_times", preparation_times)
        # print("wait_times", wait_times)
        for i in range(1, len(customers)):
            preparation_times.append(max(preparation_times[i - 1] + customers[i][1], customers[i][0] + customers[i][1]))
            wait_times.append(preparation_times[i] - customers[i][0])
            # print("preparation_times", preparation_times)
            # print("wait_times", wait_times)
        return sum(wait_times) / len(wait_times)


sl = Solution()
tc_1_lst = [[1, 2], [2, 5], [4, 3]]
print(sl.method(tc_1_lst))
print()
tc_2_lst = [[5, 2], [5, 4], [10, 3], [20, 1]]
print(sl.method(tc_2_lst))
print()
