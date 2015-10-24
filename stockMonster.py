import threading
import time
import clientpy2

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
        # Get lock to synchronize threads
        threadLock.acquire()
        # print_time(self.name, self.counter, 3)

        while(True):
            time.sleep(self.counter)
            securitiesAvailable = clientpy2.securitiesAvailable()
            securitiesAvailableArray = securitiesAvailable.split()
            for i in range(1,len(securitiesAvailableArray),4):
                print("")
                print("")
                print(securitiesAvailableArray[i])
                print(securitiesAvailableArray[i+1])
                print(securitiesAvailableArray[i+2])
                print(securitiesAvailableArray[i+3])
                order = clientpy2.ordersFor(securitiesAvailableArray[i])
                orderArray = order.split()
                for j in range(1,len(orderArray),4):
                    if(orderArray[j] == "BID"):
                        print("BID")
                        print(orderArray[j+2])
                        print(orderArray[j+3])
                    else:
                        print("ASK")
                        print(orderArray[j+2])
                        print(orderArray[j+3])

        # Free lock to release next thread
        threadLock.release()


def print_tgime(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
# thread2.start()

# Add threads to thread list
threads.append(thread1)
# threads.append(thread2)
