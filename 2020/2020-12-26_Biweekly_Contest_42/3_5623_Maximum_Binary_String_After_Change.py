# def change00to10(binary_list, start, end):
#     if binary_list[start] == 0 and binary_list[end] == 0:
#         binary_list[start] = 1
#         return True
#     return False
#
#
# def change10to01(binary_list, start, end):
#     if binary_list[start] == 1 and binary_list[end] == 0:
#         binary_list[start] = 0
#         binary_list[end] = 1
#         return True
#     return False
#
#
# def change00to01(binary_list, start, end):
#     return change00to10(binary_list, start, end) and change10to01(binary_list, start, end)
#
#
# def change10to01force(binary_list, start, end):
#     return change10to01(binary_list, start, end) or change00to01(binary_list, start, end)
#
#
# class Solution:
#
#     def method(self, binary: str) -> int:
#         self = self
#         if binary == "00":
#             return "10"
#         elif binary == "01" or binary == "11" or binary == "10":
#             return binary
#         else:
#             binary_list = [int(st) for st in binary]
#             # print(binary_list)
#             dim = len(binary_list)
#             j = dim - 1
#             while j > 0:
#                 change10to01force(binary_list, j - 1, j)
#                 j -= 1
#                 print("j =", j, binary_list)
#             i = 1
#             while i < dim:
#                 change00to10(binary_list, i - 1, i)
#                 i += 1
#                 print("i =", i, binary_list)
#             return "".join([str(integ) for integ in binary_list])
#
#
# sl = Solution()
# tc_1_bin_str = "000110"
# print(sl.method(tc_1_bin_str))
# print()
# tc_2_bin_str = "01"
# print(sl.method(tc_2_bin_str))
# print()
# tc_3_bin_str = "01111001100000110010"
# # expected "11111111110111111111"
# print(sl.method(tc_3_bin_str))
# print()
