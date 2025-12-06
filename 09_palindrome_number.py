class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        
        i = x
        s = 0

        while(i > 0):
            d = i % 10
            s = s * 10 + d
            i = i // 10
        
        if (x == s) :
            return True
        return False
       
sol = Solution()
print(sol.isPalindrome(121))  # True
print(sol.isPalindrome(-121)) # False  
print(sol.isPalindrome(10))   # False
print(sol.isPalindrome(12321)) # True