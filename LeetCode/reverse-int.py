class Solution:
    # naive approach by converting x into string for string manipulation
    def reverseString(self, x: int) -> int:
        if x > 0:
            ret = int(str(x)[::-1])
        else:
            ret = -1 * int(str(x * -1)[::-1])
        # for 32-bit overflow cases
        return ((-2**31 <= ret) and (ret <= 2**31-1)) * ret

    # stack approach push each number and pop them into a reversed list
    def reverseStack(self, x: int) -> int:
        # convert the integer to string and have cases for negative number, 0 as last number
        return None


x = 120
print(Solution().reverseString(x))
