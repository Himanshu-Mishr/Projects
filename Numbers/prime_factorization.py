#!/usr/bin/python3
# coder : Himanshu Mishra
# about : finding PRIME FACTORIZATION
# algorithm used : my own, recursion
# links : 

# takes input a number and return T/F for being prime.
def prime_check(n):
    #print(" processing....",n)
    
    i = n//2
    flag = 0

    while i > 1:
        #print("    ⇒ ",n,i)
        if n%i == 0:
            flag = 0
            #print("    ⇒ ",n,i)
            break
        i -= 1    

    else:flag = 1

    if flag == 1:return True
    else : return False
    


# the user enter a number and find all Prime Factors (if there are any) and display them.
def main():
    n = int(input("Enter the number :- "))
    while n > 1:
        
        if prime_check(n):print("   ✔",n,"Prime")
        else:print("   ✘",n,"not Prime")
        n -= 1
# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()
