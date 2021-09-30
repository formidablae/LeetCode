class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
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
