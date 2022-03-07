class RomanNumerals:

    def to_roman(val):
        vale = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        i = 0
        num = ""
        while  val > 0:
            for _ in range(val // vale[i]):
                num += syb[i]
                val -= vale[i]
            i += 1
        return num

    def from_roman(val):
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        i = 0
        num = 0
        while i < len(val):
            if i+1<len(val) and val[i:i+2] in roman:
                num+=roman[val[i:i+2]]
                i+=2
            else:
                num+=roman[val[i]]
                i+=1
        return num
