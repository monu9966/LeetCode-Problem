class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        # Start from last digits
        for i in range(n-1, -1, -1):
                
                # if digit is less than 9
                if digits[i] < 9:
                     digits[i] += 1
                     return digits
                
                # if digit is 9
                digits[i] = 0  

        # if all digit were 9
        return [1] + digits
          