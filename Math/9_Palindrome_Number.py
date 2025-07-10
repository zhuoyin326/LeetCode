class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        l = 0
        r = len(num_str)-1
        
        while l <= r :
        
            if num_str[l]!=num_str[r]:
                return False
                
            else:
                l += 1
                r -= 1
        
            return True
