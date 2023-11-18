# define an array/list of price
prices = [100, 150, 80, 90, 100,110]
# calculating length of price list
n = len(prices)
# setting spans as list/array of zeros 
spans = [0]*n
# setting first element/ day to 1
spans[0] = 1
# iterate prices from range second to the last
for i in range(1,n):
    # initialize span and index i.e. span set to 1
    span = 1
    # conditon check / backward traversal for previous day price comperision
    while(i - span) >= 0 and prices[i] >= prices[i - span]:
        span += spans[i - span]
    # storing spans value
    spans[i] = span
    
print("Stock Span list of given prices is as :- ", spans)
        