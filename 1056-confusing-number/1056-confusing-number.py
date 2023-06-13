class Solution:
    def confusingNumber(self, n: int) -> bool:
        new = []
        for num in str(n):
            if num in '23457':
                return False
            else:
                if num == '9': num = '6' 
                elif num == '6': num = '9' 
                new.append(num)

        if int(n) != int(''.join(new[::-1])):
            return True
        else:
            return False