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
        empty = ""
        while rline:
            empty += rline.strip()
            rline = sfile.readline()
        return empty
    finally:
        sock.close()

def help():
    #run("admin", "topbanana0918", "BID EA 10.2 1")
    return run("admin","topbanana0918","HELP")

def bid(ticker,price,amount):
    #run("admin", "topbanana0918", "BID EA 10.2 1")
    return run("admin","topbanana0918","BID " + ticker + " " + price + " " + amount)

def ask(ticker,price,amount):
    #run("admin", "topbanana0918", "ASK EA 10.2 1")
    return run("admin","topbanana0918","ASK " + ticker + " " + price + " " + amount)

def securitiesAvailable():
    #run("admin", "topbanana0918", "ASK EA 10.2 1")
    return run("admin","topbanana0918","SECURITIES")

def ordersFor(ticker):
    return run("admin","topbanana0918","ORDERS " + ticker)

def mySecurities():
    #run("admin", "topbanana0918", "ASK EA 10.2 1")
    return run("admin","topbanana0918","MY_SECURITIES")

def myOrders(ticker):
    return run("admin","topbanana0918","ORDERS " + ticker)

def myCash():
    return run("admin","topbanana0918","MY_CASH")

def deleteBid(ticker):
    return run("admin","topbanana0918","CLEAR_BID " + ticker)

def deleteAsk(ticker):
    return run("admin","topbanana0918","CLEAR_ASK " + ticker)

def subscribe(yesOrNo):
    if(yesOrNo):
        return run("admin","topbanana0918","SUBSCRIBE")
    else:
        return run("admin","topbanana0918","UNSUBSCRIBE")
