# def maxResult(nums, k):
#     i = 0
#     summat = 0
#     while True:
#         min_val_last_index = len(nums) - 1 - nums[::-1].index(min(nums[i + 1: min(len(nums) - 1, i + k)]))
#         summat += nums[min_val_last_index]
#         i += min_val_last_index
#         break
#     return summat
#
#
# inp1 = [1, -1, -2, 4, -7, 3]
# k1 = 2
# inp2 = [10, -5, -2, 4, 0, 3]
# k2 = 3
# inp3 = [1, -5, -20, 4, -1, 3, -6, -3]
# k3 = 2
# print(maxResult(inp1, k1))
# print(maxResult(inp2, k2))
# print(maxResult(inp3, k3))
