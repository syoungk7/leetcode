class Solution:
    def isValid(self, s: str) -> bool:  
        pairs = {'(': ')', '{':'}', '[' : ']'}
        stack=[]

        for bracket in s:
            if bracket in pairs.keys():
                stack.append(pairs[bracket])
            elif bracket in pairs.values():
                if len(stack) == 0:
                    return False
                else:
                    opp = stack.pop()
                    if opp != bracket:
                        return False

        if len(stack) == 0: 
            return True
        else: 
            return False