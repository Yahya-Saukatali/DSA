class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_list = list(magazine)
        for i in ransomNote:
            if i not in magazine_list:
                return False
            magazine_list.remove(i)
        return True

