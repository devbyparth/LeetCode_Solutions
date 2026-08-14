class Solution(object):
    def toLowerCase(self, s):
        res = []
        for char in s:
            if 'A' <= char <= 'Z':
                res.append(chr(ord(char) + 32))
            else:
                res.append(char)
        return ''.join(res)
    
    """
    Or we can just use:
        return s.lower()
    """