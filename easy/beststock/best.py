class Solution:
    def __init__(self):
        self._prices: list[int] = [2, 5, 4, 3, 1, 6, 3, 5, 8]

    def best_stock(self) -> int:
        left, right = 0, 1
        maxProfit = 0

        while right < len(self._prices):
            if self._prices[left] < self._prices[right]:
                profit = self._prices[right] - self._prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right

            right += 1

        return maxProfit


def main():
    solution = Solution()

    result = solution.best_stock()

    print("This is best stock we are passing [2, 5, 4, 3, 1, 6, 3, 5, 8]")
    print("We should return 7, which is the max profit of 1 and 8")
    print(result)


if __name__ == "__main__":
    main()
