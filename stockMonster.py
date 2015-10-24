import threading
import time
import company
import clientpy2
import ui
# import pygame
# from pygame.locals import *


class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.gui = ui.UI()
    def run(self):
        print "Starting " + self.name
        # threadLock.acquire()

        if(self.counter == 1 ):

            while(True):
                securitiesAvailable = clientpy2.securitiesAvailable()
                cash = clientpy2.myCash().split()
                cashAvailable = float(cash[1])
                securitiesAvailableArray = securitiesAvailable.split()
                toUI = []
                for i in range(1,len(securitiesAvailableArray),4):

                    companies[securitiesAvailableArray[i]].add_net_worth(securitiesAvailableArray[i+1])
                    toUI.append(float(securitiesAvailableArray[i+1])/1000000)
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

                divRatio = clientpy2.mySecurities()
                divRatioArray = divRatio.split()
                for j in range(1,len(divRatioArray),3):
                    companies[divRatioArray[j]].add_dividend_ratio(divRatioArray[j+2])
                    print("divRatio")
                    print(divRatioArray[j+2])

                self.gui.run(toUI)

                for comp in companies:
                    if(companies[comp].haveEnoughData):
                        print(companies[comp].getTicker())
                        ratio = float(companies[comp].ideal_askCost())/float(companies[comp].ideal_bidCost())
                        print("netWorthShouldBuy:  " + str(companies[comp].netWorthShouldBuy()))
                        print("Ratio")
                        print(ratio)
                        print(companies[comp].current_dividend_ratio())

                        if(companies[comp].netWorthShouldBuy() and ratio < 2.2 and cashAvailable > 50):
                            for i in range(1,5):
                                ratio = float(companies[comp].ideal_askCost())/float(companies[comp].ideal_bidCost())
                                clientpy2.bid(companies[comp].getTicker(),companies[comp].ideal_askCost(),companies[comp].ideal_askAmount())
                                print(companies[comp].getTicker())
                                print(companies[comp].ideal_askCost())
                                print(companies[comp].ideal_askAmount())
                                print(ratio)
                                companies[comp].printStock()
                                if(ratio > 1.5):
                                    break

                        elif((float(companies[comp].current_dividend_ratio()) < float(.005) and float(companies[comp].current_dividend_ratio()) != float(0.0)) or cashAvailable < 50):
                            print("selling")
                            clientpy2.ask(companies[comp].getTicker(),companies[comp].ideal_bidCost(),companies[comp].ideal_bidAmount())

                        else:
                            clientpy2.ask(companies[comp].getTicker(),companies[comp].ideal_bidCost(),companies[comp].ideal_bidAmount())

                        #giveAway on of this array
                        #giveaway = float(companies[comp].ideal_bidCost()) + .5
                        #clientpy2.ask(companies[comp].getTicker(), str(giveaway), "1")
                    # companies[securitiesAvailableArray[i]].printStock()


        # Free lock to release next thread
        # threadLock.release()

def startApp():

    securitiesAvailable = clientpy2.securitiesAvailable()
    securitiesAvailableArray = securitiesAvailable.split()
    for i in range(1,len(securitiesAvailableArray),4):

        comp = company.Company(securitiesAvailableArray[i],
                                securitiesAvailableArray[i+1],
                                securitiesAvailableArray[i+2],
                                securitiesAvailableArray[i+3])
        companies[securitiesAvailableArray[i]] = comp


    # Start new Threads
    thread1.start()
    # thread2.start()

    # Add threads to thread list
    threads.append(thread1)
    # threads.append(thread2)

threadLock = threading.Lock()

threads = []

# Create new threads
thread1 = myThread(1, "UpdateThread", 1)
# thread2 = myThread(2, "BuyThread", 2)

companies = {}
startApp()
