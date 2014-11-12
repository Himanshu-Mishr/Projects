#!/usr/bin/python3
# coder : Himanshu Mishra
# about : Factorial Finder
# algorithm used : recursion
# links : Number/factorial_finder.py
#----------------------------------------------------------

# global declaration of fact
# inorder to sync with both function
fact =  1

# factorial : this function calculate factorial using recursion
# n --> n-1 --> n-2 --> .......3 --> 2 --> 1
def factorial(n):
    global fact
    # condition to get out of recursion
    if n == 1:
        return fact

    # else do recursion
    else:
        fact = fact * n
        factorial(n-1)

# this function takes a input and gives out its factorial 
def main():
    
    # information for the user and for input
    info = """
    Program : Factorial Finder
    Enter a number to find its factorial

    > """
    n = int(input(info))

    factorial(n)
    global fact
    print("\n    The Factorial of ",n,"(n!) is ",fact,"\n")

# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()