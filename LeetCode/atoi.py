import re


class Solution:
    def myAtoi(self, string: str) -> int:

        res = re.search("^( )*[+-]?\d\d*", string)
        int_min, int_max = -2147483648, 2147483647

        if res:
            number = int(res[0])
            if int_min < number < int_max:
                return number
            elif number > 0:
                return int_max
            else:
                return int_min
        else:
            return 0


s = 'atoi 123'
print(Solution().myAtoi(s))
