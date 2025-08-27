class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        num = x
        pldm = 0
        while num > 0:
            ld = num % 10
            pldm = (pldm * 10) + ld
            num //= 10
        return pldm == x


        