class Solution:
    def method(self, students: list, sandwiches: list) -> int:
        self = self
        flag = True
        while flag:
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
            else:
                students.pop(0)
                sandwiches.pop(0)

            if len(sandwiches) == 0 or len(students) == 0:
                flag = False
            else:
                flag = False
                for pref in students:
                    if pref == sandwiches[0]:
                        flag = True
                        break
        return len(students)


sl = Solution()
tc_1_lst1 = [1, 1, 0, 0]
tc_1_lst2 = [0, 1, 0, 1]
print(sl.method(tc_1_lst1, tc_1_lst2))

print()

tc_2_lst1 = [1, 1, 1, 0, 0, 1]
tc_2_lst2 = [1, 0, 0, 0, 1, 1]
print(sl.method(tc_2_lst1, tc_2_lst2))
