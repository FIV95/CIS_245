#lists to dictionary
#stocks = ["ACLS", "BRK", "GOOG", "HOG", "INTC", "KO", "T", "XOM" "WOOF", "WMT"]
#stock_amounts = ["$123", "$150", "$170", "$50", "$67", "$83", "$46", "$105", "$87", "$115"]

#dictionary
#stocks_with_amounts = {key:value for key, value, in zip(stocks, stock_amounts)}
stocks_with_amounts = {"ACLS": 123, "BRK": 150, "GOOG": 187, "HOG": 170, "INTC": 50, "KO": 67, "T": 83, "XOM": 46, "WOOF": 105, "WMT": 115}
stocks_with_company_names = {
  "ACLS": "Axcelis Technologies Inc",
  "BRK": "Berskhire Hathaway Inc",
  "GOOG": "Google",
  "HOG": "Harley-Davidson",
  "INTC": "Intel",
  "KO": "Coca-Cola Co",
  "T": "AT&T",
  "XOM": "Exxon Mobil Corp",
  "WOOF": "Petco Health & Wellness Company",
  "WMT": "Walmart"
  }

#dictionary_with_title
main = {"This Program's Stocks": stocks_with_amounts}
#print(main)

  

#messages
primary_message = """This program contains the stock data for the following companies:

Axcelis Technologies Inc - ACLS
Berkshire Hathaway Inc - BRK
Google - GOOG
Harley-Davidson - HOG
Intel- INTC
Coca-Cola Co - KO
AT&T - T
Exxon Mobil Corp - XOM
Petco Health & Wellness Company - WOOF
Walmart -WMT

Once you are done looking up stock prices please input 'quit' to end the program.
"""

while True:
  print(primary_message)

  inquiry = input("Which company would you like to know the current price of? Please input the associated ticker symbol: ").upper()
  if inquiry == 'QUIT':
    print("Thank you for using our stock information program.")
    break
  stock_amount = stocks_with_amounts.get(inquiry)
  company_name = stocks_with_company_names.get(inquiry)
  if stock_amount == None or company_name == None:
    print('An error occured, Either we do not have the stock data for that company or you did not enter a valid ticker symbol. Please refer to the list of companies and try again.')
  else: 
    print(f'The price of a stock at {company_name} is ${stock_amount}')
  



  
  



  