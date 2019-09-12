# # Stock Prices

# You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock. 

# Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

# For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices. 

# ## Testing

# Run the test file by executing `python test_stock_prices.py`.

# You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

# ## Hints

#  For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices. 

#  So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`? 
#!/usr/bin/python

import argparse

# find_max_profit([1050, 270, 1540, 3800, 2]) //3530

def find_max_profit(prices):
  second_lowest_price=prices[0]
  current_lowest_price=prices[0]
  current_maximum_profit=0
  for i in range(len(prices)):
    if current_lowest_price>prices[i]:
      # update lowest price if it's smllaer
      second_lowest_price= current_lowest_price
      current_lowest_price=prices[i]
    # else if current max profit is smaller than the current difference
    elif current_maximum_profit< prices[i]-current_lowest_price:
      # update the current max profit
      current_maximum_profit=prices[i]-current_lowest_price
  # if current max profit is 0
  if current_maximum_profit==0:
    # return the lowest loss
    return current_lowest_price-second_lowest_price
  # return the max profit
  return current_maximum_profit
# def find_max_profit(prices):
#     max_profit = prices[1]-prices[0]
#     for x in range(len(prices)-1):
#         for y in range(x+1, len(prices)):
#             if prices[y] - prices[x] > max_profit:
#                 max_profit = prices[y] - prices[x]
#     return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))