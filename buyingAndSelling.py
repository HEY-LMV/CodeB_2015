import clientpy2
import company



def getStocks():
    companies = {}

    securitiesAvailable = clientpy2.securitiesAvailable()
    securitiesAvailableArray = securitiesAvailable.split()
    for i in range(1,len(securitiesAvailableArray),4):

        companies[securitiesAvailableArray[i]].add_net_worth(securitiesAvailableArray[i+1])
        companies[securitiesAvailableArray[i]].add_dividend_ratio(securitiesAvailableArray[i+2])

        order = clientpy2.ordersFor(securitiesAvailableArray[i])
        orderArray = order.split()
        bidCost = []
        bidAmount = []
        askCost = []
        askAmount = []
        for j in range(1,len(orderArray),4):
            if(orderArray[j] == "BID"):
                bidCost.append(orderArray[j+2])
                bidAmount.append(orderArray[j+3])
            else:
                askCost.append(orderArray[j+2])
                askAmount.append(orderArray[j+3])

        companies[securitiesAvailableArray[i]].set_bid(bidCost,bidAmount)
        companies[securitiesAvailableArray[i]].set_ask(askCost,askAmount)

getStocks()
