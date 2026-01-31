class Solution(object):
    def isPalindrome(self, s):
        # convert to lowercase and keep only letters & numbers
        s = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        # check if palindrome
        return s == s[::-1]
        
