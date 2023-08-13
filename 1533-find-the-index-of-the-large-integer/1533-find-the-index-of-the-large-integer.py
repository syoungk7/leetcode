# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        start = 0
        end = reader.length() - 1
        summ = 111

        if reader.length() < 5:
            while start < end:
                summ = reader.compareSub(start, start, end, end)
                if summ == -1: return end
                if summ == 1: return start
        
        while start < end:
            middle = start+int((end-start)/2)

            if (end - start) % 2 == 0:
                summ = reader.compareSub(start, middle-1, middle+1, end)
                if summ == 0: return middle
                else:
                    if summ == -1: start = middle+1
                    if summ == 1: end = middle-1                    
            else:
                summ = reader.compareSub(start, middle, middle+1, end)
                if summ == -1: start = middle+1
                if summ == 1: end = middle

        return end