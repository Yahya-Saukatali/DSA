class Solution(object):
    def detectCapitalUse(self, word):
        all_upper = ""
        all_lower = ""
        for char in word:
            if char.isupper():
                all_upper += char
            if char.islower():
                all_lower += char
        if all_upper == word:
            return True
        elif all_lower == word:
            return True
        elif len(all_lower) == len(word) - 1 and word[0].isupper():
            return True
        else:
            return False

