class Solution:
    def ret(self, x):
        if -2 ** 31 <= x <= 2 ** 31 - 1:
            return x
        return 0
    def reverse(self, x: int) -> int:
        _x = ''.join(list(str(x))[::-1])
        if _x[-1] == '-': return self.ret(- int(_x[:-1]))
        return self.ret(int(_x))
