#stonks
# Write code below 💖
import math
"""price_at(x) that finds the price on a given day x.
max_price(a, b) that finds the maximum price from day a to day b.
min_price(a, b) that finds the minimum price from day a to day b"""

stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

def price_at(a):
    return(stock_prices[a-1])
def max_price(x, y):
    return(max(stock_prices[x-1:y]))
def min_price(x,y):
    return(min(stock_prices[x-1:y]))

print(min_price(1,6))
print(max_price(1,6))
print(price_at(5))