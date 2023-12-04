class Solution:
    def maximumSwap(self, num: int) -> int:
        tmp = [int(i) for i in str(num)]
        n_idx, max_idx = -1, len(tmp) - 1
        
        for i in range(len(tmp)-1, -1, -1):            
            if tmp[max_idx] < tmp[i]:
                max_idx = i
            elif tmp[i] < tmp[max_idx]:
                n_idx = i
                nn_idx = max_idx

        if n_idx == -1: return num
        else:
            print(n_idx, nn_idx, max_idx)
            max_num = tmp[nn_idx]
            tmp[nn_idx] = tmp[n_idx]
            tmp[n_idx] = max_num
            return int(''.join(str(i) for i in tmp))
        
        
        
        # num = [int(x) for x in str(num)]
        # max_idx = len(num) - 1
        # xi = yi = 0
        # for i in range(len(num) - 1, -1, -1):
        #     if num[i] > num[max_idx]:
        #         max_idx = i
        #     elif num[i] < num[max_idx]:
        #         xi = i
        #         yi = max_idx
        # num[xi], num[yi] = num[yi], num[xi]
        # return int(''.join([str(x) for x in num]))