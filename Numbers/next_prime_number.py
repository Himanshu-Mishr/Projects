#!/usr/bin/python3
# coder : Himanshu Mishra
# about : Next Prime Number
# algorithm used : calculating prime numbers
# links : Numbers/next_prime_number.py

prime = 0

def primeCheck(y):
    while(True):
        y += 1
        x= y//2
        while x>1:
            if y%x == 0:
                break
            x -= 1
        else:
            print(" ⇒  Next Prime : ",y)
            global prime
            prime = y
            break

    
    

# Have the program find prime numbers until the user chooses to stop asking for the next one
def main():
    info = """
    Program Name : Next Prime Number

    Enter "next" for next prime number
    To Exit just press Enter 【 ↵ 】.
    """
    print(info)
    global prime
    try :
        prime  =  int(input("From where you want to start : "))
    except:
        prime = 1

    #print("Next Prime : ",prime)
    while input(" ⇐ ") == "next" :
        primeCheck(prime)
    else:
        print("-------------------")
        print("Exiting Program")

    return 0    

# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()
    