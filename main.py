stockName = input("what is your stock name?:")
stockCount = float(input("How many shares of stocks did you purchase?: "))
stockPrice = float(input("What is the price per share when purchasing?: "))
stockSold = float(input("How many shares did you sell?: "))
stockNewPrice = float(input("What is the price when selling it?: "))

pricePaid = stockSold * stockNewPrice
remainingStocks = stockCount - stockSold
remainingSharesTotalPrice = remainingStocks * stockNewPrice
stockProfitability = (stockSold * stockNewPrice) - (stockSold*stockPrice)

print(stockName)
print(f'Price paid for the sale: $ {pricePaid}')
print(f'Shares remaining: {remainingStocks}')
print(f'money remaining shares are worth: $ {remainingSharesTotalPrice}')
print(f'profit made in sale: ${stockProfitability}')
