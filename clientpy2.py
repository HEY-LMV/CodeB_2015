import socket
import sys

def run(user, password, *commands):
    HOST, PORT = "codebb.cloudapp.net", 17429
    
    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"
    
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

def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    
    data=user + " " + password + "\nSUBSCRIBE\n"
    
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

def help():
    #run("admin", "topbanana0918", "BID EA 10.2 1")
    run("admin","topbanana0918","HELP")

def bid(ticker,price,amount):
    #run("admin", "topbanana0918", "BID EA 10.2 1")
    run("admin","topbanana0918","BID " + ticker + " " + price + " " + amount)

def ask(ticker,price,amount):
    #run("admin", "topbanana0918", "ASK EA 10.2 1")
    run("admin","topbanana0918","ASK " + ticker + " " + price + " " + amount)

def securitiesAvailable():
    #run("admin", "topbanana0918", "ASK EA 10.2 1")
    run("admin","topbanana0918","SECURITIES")

def ordersFor(ticker):
    run("admin","topbanana0918","ORDERS " + ticker)

def mySecurities():
    #run("admin", "topbanana0918", "ASK EA 10.2 1")
    run("admin","topbanana0918","MY_SECURITIES")

def myOrders(ticker):
    run("admin","topbanana0918","ORDERS " + ticker)

def myCash():
    run("admin","topbanana0918","MY_CASH")

def deleteBid(ticker):
    run("admin","topbanana0918","CLEAR_BID " + ticker)

def deleteAsk(ticker):
    run("admin","topbanana0918","CLEAR_ASK " + ticker)

def subscribe(yesOrNo):
    if(yesOrNo):
        run("admin","topbanana0918","SUBSCRIBE")
    else:
        run("admin","topbanana0918","UNSUBSCRIBE")
