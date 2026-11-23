class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev=""
        for ch in s.lower():
            if ch.isalnum():
                rev+=ch
        if rev==rev[::-1]:
            return True
        return False
        