class Solution:
    def expand(self, s: str) -> List[str]:

        def summmmm(aaa: str, lsttt: list):
            new = []
            if len(lsttt) == 0 and len(aaa) == 1: 
                new.append(aaa)
                return new
            elif len(lsttt) == 0 and len(aaa) != 1: 
                for i in sorted(aaa.split(',')): new.append(i)

            elif len(lsttt) != 0 and len(aaa) == 1:
                for j in lsttt: new.append(aaa + j)
            else:
                for k in sorted(aaa.split(',')):
                    for j in lsttt: new.append(k + j)
            return new

        lst, lsttt = [], []
        for i in s.split("}"):
            if i.isalpha(): 
                lst.append(i)
            else:
                for j in i.split('{'): lst.append(j)
        
        if len(lst) == 1: 
            return lst
        else:
            for i in lst[::-1]:
                if i != "": 
                    lsttt = summmmm(i, lsttt)

        return lsttt
