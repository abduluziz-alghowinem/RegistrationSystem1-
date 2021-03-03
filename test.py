import time
def contdown(t):
    while t>0:
        print(t)
        t-=1
        time.sleep(1)
    print("zeroooo")

string = f"{contdown(10)}"

