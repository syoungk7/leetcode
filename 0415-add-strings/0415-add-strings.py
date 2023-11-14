class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        add_Char = 0
        lst_Char = []
        ord_0 = ord('0')
        
        while num1 != '' or num2 != '' or add_Char < 0:
            if len(num1) > 0:
                add_Char += ord(num1[-1]) - ord_0
                num1 = num1[:-1]
            
            if len(num2) > 0:
                add_Char += ord(num2[-1]) - ord_0
                num2 = num2[:-1]           
            
            lst_Char.append(chr(add_Char % 10 + ord_0))
            add_Char = add_Char // 10

            if num1 == '' and num2 == '' and add_Char != 0:
                lst_Char.append(chr(add_Char + ord_0))

        return "".join(lst_Char)[::-1]
