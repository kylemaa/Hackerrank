import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # have to specify the int type of the dictionary before assigning the definition an integer.
        some_dictionary = collections.defaultdict(int)
        for char in magazine:
            some_dictionary[char] += 1
        for char in ransomNote:
            some_dictionary[char] -= 1
            if some_dictionary[char] < 0:
                return False
        return True
