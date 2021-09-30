class Solution:
    def isValid(self, s: str) -> bool:
        def balanced(st_list, i=0):
            if i >= len(st_list):
                return len(st_list) == 0
            if i >= 0 and i + 1 < len(st_list) and st_list[i] == "(" and st_list[i + 1] == ")":
                st_list.pop(i + 1)
                st_list.pop(i)
                return balanced(st_list, i - 1)
            elif i >= 0 and i + 1 < len(st_list) and st_list[i] == "[" and st_list[i + 1] == "]":
                st_list.pop(i + 1)
                st_list.pop(i)
                return balanced(st_list, i - 1)
            elif i >= 0 and i + 1 < len(st_list) and st_list[i] == "{" and st_list[i + 1] == "}":
                st_list.pop(i + 1)
                st_list.pop(i)
                return balanced(st_list, i - 1)
            return balanced(st_list, i + 1)

        return balanced(list(s))


# sl = Solution()
# inp1 = "()"
# inp2 = "()[]{}"
# inp3 = "(]"
# inp4 = "([)]"
# inp5 = "{[]}"
# print(sl.isValid(inp1))
# print(sl.isValid(inp2))
# print(sl.isValid(inp3))
# print(sl.isValid(inp4))
# print(sl.isValid(inp5))