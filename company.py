
class Company:

	def __init__(self, ticker, net_worth, dividend_ratio, volatility):
		self.ticker = ticker
		self.net_worth = [net_worth]
		self.dividend_ratio = [dividend_ratio]
		self.volatility = volatility

	def add_net_worth(self, net_worth):
		self.net_worth.append(net_worth)

	def add_dividend_ratio(self, dividend_ratio):
		self.dividend_ratio.append(dividend_ratio)

	def set_bid(self, bidCost, bidAmount):
		self.bidCost = bidCost
		self.bidAmount = bidAmount

	def set_ask(self, askCost, askAmount):
		self.askCost = askCost
		self.askAmount = askAmount

	def current_net_worth(self):
		return self.net_worth[len(self.net_worth)-1]

	def current_dividend_ratio(self):
		return self.dividend_ratio[len(self.dividend_ratio)-1]

	def current_bidCost():
		return self.bidCost

	def current_bidAmount():
		return self.bidAmount

	def current_askCost():
		return self.askCost

	def current_askAmount():
		return self.askAmount
