#!/usr/bin/python3
# coder : Himanshu Mishra
# about : count the number of words in a string
# algorithm used : counting words
# links : Text/count_word.py

# this function counts the number of words in string
def main():
    astring = input("Enter sentence : ")
    alist = astring.split()
    print("Number of words : ",len(alist))
    


# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()