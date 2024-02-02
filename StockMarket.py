import random

class Stock:
    def __init__(self, symbol, initial_price):
        self.symbol = symbol
        self.price = initial_price
        self.quantity =0

    def update_price(self):
        # Simulate random price changes
        self.price += random.uniform(-2, 2)

class StockMarketSimulator:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.stocks = {}

    def buy_stock(self, symbol, quantity):
        if symbol in self.stocks:
            stock = self.stocks[symbol]
            cost = stock.price * quantity
            if self.balance >= cost:
                self.balance -= cost
                print(f"Bought {quantity} shares of {symbol}")
            else:
                print(f"Insufficient funds to buy {quantity} shares of {symbol}")
        else:
            print(f"Stock {symbol} not found.")

    def sell_stock(self, symbol, quantity):
        if symbol in self.stocks:
          stock = self.stocks[symbol]
          if quantity <= stock.quantity:
            revenue = stock.price * quantity
            self.balance += revenue
            print(f"Sold {quantity} shares of {symbol}")
        else:
            print(f"Cannot sell {quantity} shares of {symbol}")

    def simulate_day(self):
        for stock in self.stocks.values():
            stock.update_price()

    def display_portfolio(self):
        print(f"Balance: ${self.balance}")
        print("Stock Portfolio:")
        for symbol, stock in self.stocks.items():
            print(f"{symbol}: {stock.price}")


apple_stock = Stock("AAPL", initial_price=150)
google_stock = Stock("GOOGL", initial_price=2500)

simulator = StockMarketSimulator(initial_balance=10000.0)
simulator.stocks = {"AAPL": apple_stock, "GOOGL": google_stock}

# Simulate trading for 10 days
for day in range(1, 11):
    print(f"Day {day}")
    simulator.simulate_day()

    # Buy or sell stocks randomly for demonstration purposes
    if random.choice([True, False]):
        symbol = random.choice(["AAPL", "GOOGL"])
        quantity = random.randint(1, 10)
        if random.choice([True, False]):
            simulator.buy_stock(symbol, quantity)
        else:
            simulator.sell_stock(symbol, quantity)

    simulator.display_portfolio()
    print("=" * 30)
