class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.int_lst = []

    def next(self, val: int) -> float:
        self.int_lst.append(val)
        len_lst = len(self.int_lst)
        if len_lst <= self.size:
            return sum(self.int_lst) / len_lst
        else:
            self.int_lst.pop(0)
            return sum(self.int_lst) / self.size
        # else:
        #     return sum(self.int_lst[-self.size:]) / self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)