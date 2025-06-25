class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        
        while n >= 5:
            n //= 5

            count += n
        return count
        

        '''
        n = 100                  n = 3                  n = 5
        n = 100 // 5 ---> 20     n = 3 // 5 ---> 0      n = 5 // 5
        count = 20               count = 0              count = 1
        return 20                 return 0              return 1
        '''