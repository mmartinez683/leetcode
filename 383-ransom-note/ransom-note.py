class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        ransomNote = list(ransomNote)
        magazine = list(magazine)

        for char in ransomNote:
            if char in magazine:
                magazine.remove(char)
            else:
                return False
        return True 