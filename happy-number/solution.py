class Solution:
    def getSum(self, n):
        sum = 0
        while n != 0:
            sum += pow(n % 10, 2)
            n //= 10
        return sum
    
    def isHappy(self, n: int) -> bool:
        ans = self.getSum(n)
        next_ans = self.getSum(ans)
        while ans != next_ans:
            ans = self.getSum(ans)
            next_ans = self.getSum(self.getSum(next_ans))
        return ans == 1
