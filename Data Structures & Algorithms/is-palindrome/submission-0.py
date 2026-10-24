class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(i for i in s if i.isalnum())
        if new_str.lower() == new_str[::-1].lower():
            return True
        else:
            return False
        
