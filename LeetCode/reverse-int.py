class Solution:
    # naive approach by converting x into string for string manipulation
    def reverseString(self, x: int) -> int:
        if x > 0:
            ret = str(x)[::-1]
        else:
            ret = -1 * int(str(x * -1)[::-1])
        return ret

    # stack approach push each number and pop them into a reversed list
    def reverseStack(self, x: int) -> int:
        if x > 0:
            ret = str(x)[::-1]
        else:
            ret = -1 * int(str(x * -1)[::-1])
        return ret


x = -123
print(Solution().reverseString(x))
