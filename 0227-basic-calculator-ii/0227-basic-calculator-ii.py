class Solution:
    def calculate(self, s: str) -> int:
        oper = []
        numb = []
        pre_idx = 0

        #s = s.replace(" ", '')
        calc = {'+': lambda i, j: i + j, '-': lambda i, j: i - j, '*': lambda i, j: i * j, '/': lambda i, j: i / j}

        for idx, val in enumerate(s):
            if val and val in ['+', '-', '*', '/']:
                numb.append(s[pre_idx: idx])
                oper.append(val)
                pre_idx = idx+1
            else: pass

            if idx == len(s)-1:
                numb.append(s[pre_idx::])

            if len(oper) >= 2 and len(numb) == 3:
                if oper[1] in ['+', '-'] or oper[0] == '/':
                    tmp = calc[oper[0]](int(numb[0]), int(numb[1]))
                    oper.pop(0)
                    numb.pop(0)
                    numb[0] = int(tmp)
                else:
                    tmp = calc[oper[1]](int(numb[1]), int(numb[2]))
                    oper.pop(1)
                    numb.pop(1)
                    numb[1] = int(tmp)
            #print(numb)
        if len(oper) == 1:
            return int(calc[oper[0]](int(numb[0]), int(numb[1])))
        return int(numb[0])