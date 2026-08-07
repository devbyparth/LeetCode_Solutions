class Solution(object):
    def countPrimes(self, n):
        my_arr = [1] * n
        for i in range(2, n):
            if my_arr[i] == 1:
                for j in range(i ** 2, n, i):
                    my_arr[j] = 0

        count = 0
        for i in range(2, n):
            if my_arr[i] == 1:
                count += 1

        return count