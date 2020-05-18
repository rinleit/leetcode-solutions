class Solution:
    def intToRoman(self, num: int) -> str:
        # 1 <= num <= 3999
        pass1 = ('', 'M', 'MM', 'MMM')[int(num/1000)] 
        pass2 = ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM')[int(num%1000/100)]
        pass3 = ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC')[int(num%100/10)]
        pass4 = ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX')[num%10]
        return pass1 + pass2 + pass3 + pass4