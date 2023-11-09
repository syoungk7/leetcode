class Solution:
    def isValid(self, s: str) -> bool:  
        pairs = {'(': ')', '{':'}', '[' : ']'}
        stack=[]

        for cha in s:
            if cha in pairs.keys():
                stack.append(pairs[cha])
            elif len(stack) == 0 or cha != stack.pop():
                    return False

        return len(stack) == 0
        
#         for cha in s:
#             if cha in pairs:
#                 stack.append(cha)
#             elif len(stack) == 0 or cha != pairs[stack.pop()]:
#                 return False

#         return len(stack) == 0