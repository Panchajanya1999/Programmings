class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # sort the prices list
        prices.sort()
        # if the sum of first and second chocolate is more than the 
        # money, we will not buy anything. Return the money
        if prices[0] + prices[1] > money:
            return money
        # else, return the money left with us after buying the first and second 
        # chocolate
        return money - (prices[0] + prices[1])
