class Solution:
    def confusingNumber(self, n: int) -> bool:
        new = []
        for num in str(n):
            if num in '23457': return False
            
            if num in '96':
                if num == '9': num = '6' 
                else: num = '9' 
            new.append(num)

        if int(n) != int(''.join(new[::-1])): return True
        
        return False