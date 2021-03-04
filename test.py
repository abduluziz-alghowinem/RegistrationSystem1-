import time
def countdown(start):
    while start > 0:
        msg = "New year starts in: {} seconds".format(start)
        print(msg)
        time.sleep(1)
        start -= 1
    print(msg)
countdown(10)