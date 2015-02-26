#!/usr/bin/python3
"""
 coder : Himanshu Mishra
 about : count the number of words in a string
 algorithm used : counting words
 links : Text/count_word.py
"""


def main():
    """main function"""
    print("~ Word-O-Counter (Enter file name or a sentence) ~")
    file_name = input("Enter full path of file : ")
    alist = []
    x = 0
    try:
        f = open(file_name)
    except Exception:
        print("File Not Found")
    else:
        alist = f.read().split()
        x = 1
    if x != 1:
        astring = input("Enter sentence : ")
        alist = astring.split()

    print("Number of words : ", len(alist))
# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()
