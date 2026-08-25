# Brute Force
prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]

# n = len(prices)

# max_profit = 0

# for i in range(n):
#   for j in range(i+1,n):
#     if prices[j] > prices[i]: 
#       max_profit = max(prices[j]-prices[i], max_profit)

# print(max_profit)

# Time Complexity : O(n^2), Space complexity: O(1)
# Gives TLE not recommended

# Optimal Solution

prices = [7,1,5,3,6,4]

max_profit = 0
min_price = float("inf")

for price in prices:
  min_price = min(price, min_price)
  max_profit = max(max_profit, price - min_price)

print(max_profit)

# Time Complexity : O(n), Space complexity: O(1)

# Code explanation:

# The max_profit variable is initialized to 0, representing the maximum profit that can be obtained by selling the stock.
# The min_price variable is initialized to infinity, representing the minimum price seen so far.
# The for loop iterates through the prices array, updating min_price and max_profit whenever a new minimum price is found or a new maximum profit is obtained.
# The max_profit variable is then printed, representing the maximum profit that can be obtained by selling the stock.

