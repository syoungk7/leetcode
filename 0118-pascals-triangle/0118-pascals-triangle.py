class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # output lst
        output = [[1] * (i+1) for i in range(numRows)]
        #print(output)
        for i in range(numRows):
            for j in range(1, i):
                output[i][j] = output[i-1][j-1] + output[i-1][j]
                #print(output)
        return output