import time

def alarm():
    print("Welcome to python alram clock : ")
    print("Enter time as HH MM SS")
    x = input(" --> ")
    spot = x.split(" ")
    while True:
        if spot[0] == str(time.localtime()[3]) and spot[1] == str(time.localtime()[4]):
            print("ho ho ... wake yaar")
            break
if __name__ == '__main__':
    alarm()


