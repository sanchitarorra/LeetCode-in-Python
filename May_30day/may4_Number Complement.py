class Solution:
    def findComplement(self, num: int) -> int:
        bit = 1
        temp = num
        while temp:
            num = num ^ bit
            bit = bit << 1
            temp = temp >> 1
        return num