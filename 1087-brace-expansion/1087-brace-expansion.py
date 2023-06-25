class Solution:
    def expand(self, s: str) -> List[str]:

        def summmmm(aaa: str, lsttt: list):
            new = []
            if len(lsttt) == 0:
                if len(aaa) == 1:
                    new.append(aaa)
                    return new
                else:
                    for i in sorted(aaa.split(',')):
                        new.append(i)
            else:
                if len(aaa) == 1:
                    for j in lsttt:
                        new.append(aaa + j)
                else:
                    for k in sorted(aaa.split(',')):
                        for j in lsttt:
                            new.append(k + j)
            return new

        lst = []
        for i in s.split("}"):
            if i.isalpha():
                lst.append(i)
            else:
                a = i.split('{')
                for j in a:
                    lst.append(j)
        
        lsttt = []
        if len(lst) == 1:
            return lst
        else:
            lst2 = lst[::-1]
            for i in lst2:
                if i != "":
                    lsttt = summmmm(i, lsttt)
        return lsttt
