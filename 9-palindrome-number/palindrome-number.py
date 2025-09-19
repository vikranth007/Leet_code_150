class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        dup = x

        while x > 0:
            ld = x % 10
            rev = (rev * 10) + ld
            x = x // 10
        if dup == rev:
            return True
        else:
            return False
        