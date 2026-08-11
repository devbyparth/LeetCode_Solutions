class Solution(object):
    def canConstruct(self, ransomNote, magazine):

        magCheck = {}
        for char in magazine:
            magCheck[char] = magCheck.get(char, 0) + 1

        for char in ransomNote:
            if char in magCheck and magCheck[char] > 0:
                magCheck[char] -= 1
            else:
                return False

        return True