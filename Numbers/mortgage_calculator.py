#!/usr/bin/python3
# coder : Himanshu Mishra
# about : Mortgage Calculator -how long it will take the user to pay back the loan.
# 
# algorithm used : Mortgage return concept
# links : Numbers/mortgage_calculator.py 


# this function calculates the time taken to pay back the loan
def main():

    # information for the user
    info = '''
    Program : calculates the time taken to pay back loan

    Input : Total Loan Taken 
          : Nominal Rate
          : Amount paid back every month
    '''
    print(info)

    totalAmount = int(input("Total Amount :"))
    interest = int(input("Nominal Rate : "))/100
    payment = int(input("Amount paid back every month : "))
    
    # count : to count months
    count = 0

    # effective rate
    r = 0
    
    # loop run till no ammount is left to paid
    while totalAmount > 0:
        # Calculating Effective rate
        r = (1 + interest/12)**(1/12)  - 1 
        
        count += 1
        totalAmount += totalAmount * r
        totalAmount -= payment
        
        if totalAmount < 0:
            print("\nTotal months taken = ",count)
            break
        
        print("amount left after Month = %d || Amount Left = %.2f || Effective Rate = %.4f"%(count,totalAmount, r))

# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()