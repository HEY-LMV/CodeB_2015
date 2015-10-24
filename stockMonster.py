import threading
import time
import company
import clientpy2

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        threadLock.acquire()

        while(True):
            time.sleep(self.counter)
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

                companies[securitiesAvailableArray[i]].printStock()
        # Free lock to release next thread
        threadLock.release()

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
# thread2 = myThread(2, "Thread-2", 2)

companies = {}
startApp()
