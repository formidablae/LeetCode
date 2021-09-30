class Solution:
    def method(self, int_arg: int, lst_arg: list,  str_arg: str) -> int:
        self = self
        a = list(map(str, str_arg.split()))
        b = str_arg[::-1]
        c = "-".join(lst_arg)
        return [a, b, c]


sl = Solution()
tc_1_int = 1
tc_1_lst = ["a", "b", "c"]
tc_1_str = "abc"
print(sl.method(tc_1_int, tc_1_lst, tc_1_str))
