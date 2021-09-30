# class Solution:
#     def minOperations(self, target: list, arr: list) -> int:
#         self = self
#         # target_set = set(target)
#         i = 0
#         found_index = 0
#         while i < len(arr):
#             if arr[i] not in target[found_index:]:
#                 arr.pop(i)
#             else:
#                 found_index = max(found_index, target.index(arr[i]) + 1)
#                 i += 1
#                 if found_index == len(target):
#                     arr = arr[0:i]
#                     break
#         i = 0
#         j = 0
#         adds = 0
#         while i < len(target) and j < len(arr):
#             left = target[i]
#             right = arr[j]
#             if left != right:
#                 adds += 1
#             else:
#                 j += 1
#             i += 1
#         if i < len(target):
#             adds += len(target) - i
#         return adds
#
#
# sl = Solution()
# target_1_lst = [5, 1, 3]
# array_1_lst = [9, 4, 2, 3, 4]
#
# target_2_lst = [6, 4, 8, 1, 3, 2]
# array_2_lst = [4, 7, 6, 2, 3, 8, 6, 1]
# print("Expected 2, got", sl.minOperations(target_1_lst, array_1_lst))
# print("Expected 3, got", sl.minOperations(target_2_lst, array_2_lst))
