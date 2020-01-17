class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct = {}
        max_length = start = 0
        # enumerate the character of the string
        for k, v in enumerate(s):
            # if the character is already existed in the dictionary, then change the starting position to that character's position
            if v in dct:
                sums = dct[v]+1
                if sums > start:
                    start = sums
            # the difference of the index and starting is the length of the substring
            num = k - start + 1
            if num > max_length:
                max_length = num
            dct[v] = k
        return max_length
