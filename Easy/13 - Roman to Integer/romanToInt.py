class Solution:
    def romanToInt(self, s: str) -> int:
        roman_chars={"I":1, "V":5,"X":10, "L":50,"C":100,"D":500,"M":1000}
        sum=0
        if len(s)>15 or len(s)<1:
            return
        for i in s:
            if i not in roman_chars:
                return
        s=s.replace('IV', "IIII")
        s=s.replace("IX","VIIII")
        s=s.replace("XL","XXXX")
        s=s.replace("XC","LXXXX")
        s=s.replace("CD","CCCC")
        s=s.replace("CM", "DCCCC")
        for i in s:
            sum=sum+roman_chars[i]
        return sum