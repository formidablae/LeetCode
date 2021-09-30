# class Solution:
#     def method(self, apples: list, days: list) -> int:
#         self = self
#         days_eating = set()
#         day = 1
#         for i in range(len(apples)):
#             if len(days_eating) == 0 or max(days_eating) <= day:
#                 days_eating |= set(range(day, min(day + days[i], day + apples[i])))
#             elif max(days_eating) > day:
#                 # print("enter elif")
#                 limit0 = 0
#                 if apples[i] + max(days_eating) < days[i]:
#                     # print("enter if elif")
#                     limit0 = apples[i] + max(days_eating) - day
#                 elif day + days[i] > max(days_eating):
#                     # print("enter elif elif")
#                     limit0 = min(apples[i] + max(days_eating) - day, days[i])
#                 else:
#                     # print("enter elif else")
#                     limit0 = days[i] - max(days_eating)
#
#                 days_eating |= set(range(max(days_eating), day + limit0))
#
#             # print("day:", day, "grown today:", apples[i], "rotting in:", days[i], days_eating)
#             day += 1
#         return len(days_eating)
#
#
# class Solution:
#     def method(self, apples: list, days: list) -> int:
#         self = self
#         length = 0
#         lastday = 0
#         day = 1
#         for i in range(len(apples)):
#             if length == 0 or lastday <= day:
#                 length = min(0, min(day + days[i], day + apples[i]) - day)
#                 lastday = max(lastday, day + apples[i] - 1)
#             elif lastday > day:
#                 limit0 = 0
#                 if apples[i] + lastday < days[i]:
#                     limit0 = apples[i] + lastday - day
#                 elif day + days[i] > lastday:
#                     limit0 = min(apples[i] + lastday - day, days[i])
#                 else:
#                     limit0 = days[i] - lastday
#
#                 length = min(0, day + limit0 - max(days_eating))
#                 lastday = max(lastday, day + limit0)
#             day += 1
#         return length
#
#
# sl = Solution()
# apples1 = [1, 2, 3, 5, 2]
# days1 = [3, 2, 1, 4, 2]
# print(sl.method(apples1, days1))
# print()
# apples2 = [3, 0, 0, 0, 0, 2]
# days2 = [3, 0, 0, 0, 0, 2]
# print(sl.method(apples2, days2))
# print()
# apples2 = [9, 10, 1, 7, 0, 2, 1, 4, 1, 7, 0, 11, 0, 11, 0, 0, 9, 11, 11, 2, 0, 5, 5]
# days2 = [3, 19, 1, 14, 0, 4, 1, 8, 2, 7, 0, 13, 0, 13, 0, 0, 2, 2, 13, 1, 0, 3, 7]
# print(sl.method(apples2, days2))
# print()
