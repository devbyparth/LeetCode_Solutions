class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        reverse_num = 0
        temp = x
        
        while temp:
            reverse_num = reverse_num * 10 + temp % 10
            temp = temp // 10

        if reverse_num == x:
            return True
        else:
            return False