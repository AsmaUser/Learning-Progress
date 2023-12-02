#Palindrome Number:
class Solution(object):
    def isPalindrome(self, x):
        s_x= str(x)
        return s_x == s_x[::-1]
   