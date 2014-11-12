#!/usr/bin/python3
# coder : Himanshu Mishra
# about : Check if Palindrome
# algorithm used : Algorithms used in this program
# links : Text/palindrome_string.py

# Check if Palindrome
def main():
    info = '''
    Program : Check if Palindrome

    '''
    print(info)
    astring = input("Enter the string to check : ")

    x = list(astring)
    y = list(astring)
    y.reverse()
    
    if x[0:] == y[0:]:
        print("Entered string is Palindrome ✔")
    else:
        print("Not Palindrome ✘")

# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()