class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # create a list of digits which are 3-same-digit
        dig = ['000', '111', '222', '333', '444', '555', '666', '777', '888', '999']
        # check if a same digit exists in the number
        res = [i for i in dig if i in num]
        # return the largest good integer
        return max(res) if res else ''
