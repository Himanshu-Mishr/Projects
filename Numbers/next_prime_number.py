#!/usr/bin/python3
# coder : Himanshu Mishra
# about : Next Prime Number
# algorithm used : calculating prime numbers
# links : Numbers/next_prime_number.py
# -------------------------------------------------------

# 
# global declaration of prime varible 
# inorder to sync with both function
prime = 0

# calculates next prime 
# Parameter : y = previous prime number
def primeCheck(y):

    # while runs till the next prime number is found
    while(True):
        # incrementing to next number
        y += 1

        # logic : number above y//2 is required for division
        x= y//2

        while x>1:
            if y%x == 0:
                break
            x -= 1
        
        else:
            print(" ⇒  Next Prime : ",y)
            
            # sync the global prime number
            global prime
            prime = y
            break

    
    

# Have the program find prime numbers until 
# the user chooses to stop asking for the next one
def main():
    
    # printing information for the user
    info = """
    Program Name : Next Prime Number

    Enter "next" for next prime number
    To Exit just press Enter 【 ↵ 】.
    """
    print(info)
    
    # using global 
    global prime

    # asking user from where he/she wants to starts
    try :  
        prime  =  int(input("From where you want to start : "))
    except:
        # default start 1 , this doesn't mean 1st prime is 1 :P
        prime = 1

    # while keeps running as user enter "next" anything other 
    # than "next" will stop the loop and excutes the else block statement  
    while input(" ⇐ ") == "next" :
        primeCheck(prime)
    
    else:
        print("-------------------")
        print("Exiting Program")

    return 0    

# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()
    
