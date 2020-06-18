#!/usr/bin/python

import argparse

def find_max_profit(prices):
  maxim = prices[1] - prices[0]
  length = len(prices)
  for i in range(length):
    for j in range(length - 1):
      if prices[j+1] - prices[i] > maxim and j + 1 > i:
        maxim = prices[j + 1] - prices[i]
  
  return maxim



if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))