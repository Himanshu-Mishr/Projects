#!/usr/bin/python3
"""
 Coder : Himanshu Mishra (himanshu.m786@gmail.com)
 About : Fibonacci Sequence - 
            Enter a number and have the program generate the 
            Fibonacci sequence to that number or to the Nth number
 
 Link : https://github.com/Himanshu-Mishr/Projects/Numbers
"""

def main():
    
    # taking input n. (number of fibo series to produce) 
    n = int(input("Enter the Nth number : "))

    old_number = 0
    current_number = 1
    
    # term = to remember ith term being calculated 
    term = 0
    
    while(n>=1):  # loop runs "n" times.
        
        n -= 1
        term += 1
        

        print(" %dth term => "%(term),old_number)
        
        # algorithms
        next_number = current_number + old_number
        old_number = current_number
        current_number = next_number

# This is the standard boilerplate that calls the main() function. 
if __name__ == '__main__':
    main()
