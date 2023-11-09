class Solution:
    def isValid(self, s: str) -> bool:  
        pairs = {'(': ')', '{':'}', '[' : ']'}
        stack=[]

        for cha in s:
            if cha in pairs.keys():
                stack.append(pairs[cha])
            elif cha in pairs.values():
                if len(stack) == 0:
                    return False
                else:
                    opp = stack.pop()
                    if opp != cha:
                        return False

        if len(stack) == 0: 
            return True
        else: 
            return False