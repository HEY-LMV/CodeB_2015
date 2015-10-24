import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):

        if(counter == 1):
            while(true):
                HOST, PORT = "codebb.cloudapp.net", 17429

                data="admin" + " " + "topbanana0918" + "MY_Cash"

                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                    sock.connect((HOST, PORT))
                    sock.sendall(data)
                    sfile = sock.makefile()
                    rline = sfile.readline()
                    while rline:
                        print(rline.strip())
                        rline = sfile.readline()
                finally:
                    sock.close()



        print "Starting " + self.name
        # Get lock to synchronize threads
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # Free lock to release next thread
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)
