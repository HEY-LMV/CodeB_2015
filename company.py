
class Company:

	def __init__(self, ticker, net_worth, dividend_ratio, volatility):
		self.ticker = ticker
		self.net_worth = [net_worth]
		self.slope = [net_worth]
		self.dividend_ratio = [dividend_ratio]
		self.volatility = volatility

	def getTicker(self):
		return self.ticker

	def add_net_worth(self, net_worth):
		self.net_worth.append(net_worth)
		if(len(self.net_worth)%10 == 0):
			print("ADD")
			self.slope.append(net_worth)

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

	def ideal_bidCost(self):
		return self.bidCost[len(self.bidCost)-1]

	def ideal_askCost(self):
		return self.askCost[0]

	def current_bidCost(self):
		return self.bidCost

	def current_bidAmount(self):
		return self.bidAmount

	def current_askCost(self):
		return self.askCost

	def current_askAmount(self):
		return self.askAmount

	def printStock(self):
		print("Name: " + self.ticker)
		print("Net Worth: " + self.net_worth[len(self.net_worth)-1])
		print("Div Ratio: " + self.dividend_ratio[len(self.dividend_ratio)-1])
		print("Volatility: " + self.volatility)

	def haveEnoughData(self):
		return len(self.slope) >= 5

	def netWorthShouldBuy(self):
		if(len(self.slope) < 5):
			print("---- Just print False ----")
			return False

		print(self.slope[len(self.slope)-1])
		print(self.slope[len(self.slope)-2])
		print(self.slope[len(self.slope)-3])
		print(self.slope[len(self.slope)-4])
		print(self.slope[len(self.slope)-5])

		z = float(self.slope[len(self.slope)-1])
		y = float(self.slope[len(self.slope)-2])
		x = float(self.slope[len(self.slope)-3])
		w = float(self.slope[len(self.slope)-4])
		v = float(self.slope[len(self.slope)-5])

		difZY = z - y
		difYX = y - x
		difXW = x - w
		difWV = w - v

		if(difZY < 0 and difYX  < 0 and difXW < 0):
			print("Case1")
			return False
		elif(difZY < 0 and difYX  < 0 and difXW > 0 and difWV > 0):
			print("Case2")
			return False
		elif(difZY < 0 and difYX  < 0 and difXW < 0 and difWV < 0):
			print("Case3")
			return False
		elif(difZY > 0 and difYX  > 0 and difXW > 0 and difWV > 0):
			print("Case4")
			return True
		elif(difZY < 0 and difYX  > 0 and difXW > 0 and difWV > 0):
			print("Case5")
			return True
		else :
			print("Case6")
			return True
