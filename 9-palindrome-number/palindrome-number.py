class Solution:
    def isPalindrome(self, x: int) -> bool:
        revnum = 0 # --> Store my reversed number 123 ---> 321
        dup = x # ----> current x

        while x > 0:
            id = x % 10   # ---> 121  % 10 = 1,---> 12 % 10 = 2, ---> 1 % 10 = 1 
            revnum = (revnum * 10) + id  # cur 0 * 10 + 1 = 1, --> 1 * 10 + 2 = 12, -->12 * 10 + 1 = 121 ---> it is my revnum
            x = x // 10  #---> 121 // 10 = 12, 12 // 10 = 1, 1 // 10 = 0
        
        if dup == revnum:   # ---> dum = 1 2 1 == 1 2 1 return True / != return False
            return True
        else:
            return False

        