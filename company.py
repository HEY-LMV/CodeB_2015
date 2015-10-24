import stockMonster

class Company:

	def _init_(ticker, net_worth, dividend_ratio, volatility, bid, ask):
		self.ticker = ticker
		self.net_worth = [net_worth]
		self.dividend_ratio = [dividend_ratio]
		self.volatility = volatility
		self.bid = [bid]
		self.ask = [ask]

	def add_net_worth(self, net_worth):
		self.net_worth.append(net_worth)

	def add_dividend_ratio(self, dividend_ratio):
		self.dividend_ratio.append(dividend_ratio)

	def add_bid(self, bid):
		self.bid.append(bid)

	def add_bid(self, ask):
		self.ask.append(ask)

	def current_net_worth():
		return self.net_worth[net_worth._len_()]

	def current_dividend_ratio():
		return self.dividend_ratio[dividend_ratio._len_()]

	def current_bid():
		return self.bid[bid._len_()]

	def current_ask():
		return self.ask[ask._len_()]