#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

def eating_cookies(n, cache=None):
  if not cache:
    cache=[0 for i in range(n+1)]  
  if n<0:  
    return 0
  if n <= 1:
    return 1
  if not cache[n]:
    # if the result is not found, record that result
    cache[n]=eating_cookies(n-1,cache)+eating_cookies(n-2,cache)+eating_cookies(n-3,cache)
  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')