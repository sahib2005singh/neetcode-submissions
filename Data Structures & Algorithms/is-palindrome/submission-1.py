class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = "".join(i for i in s if i.isalnum()).lower()
        
        left = 0
        right = len(new_str) - 1

        while right > left:
            if new_str[left] == new_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True


