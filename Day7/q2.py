def max_profit_with_condition(prices):
  min_price=prices[0]
  max_profit=0

  for price in prices[1:]:
    profit=price-min_price
    if profit>=2:
      max_profit=max(max_profit,profit)
    min_price=min(min_price,price)
  return max_profit
n=int(input())
prices=list(map(int,input().strip()))

prices=[int(d) for d in str(prices[0])] if len(prices)==1 else prices
print(max_profit_with_condition(prices))