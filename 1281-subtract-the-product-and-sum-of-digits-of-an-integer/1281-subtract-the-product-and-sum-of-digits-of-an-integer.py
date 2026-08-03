class Solution(object):
    def subtractProductAndSum(self, n):
        
        product = 1
        total = 0
        
        while n > 0:
            product = product * (n % 10)
            total = total + (n % 10)
            n = n // 10
        
        return product - total