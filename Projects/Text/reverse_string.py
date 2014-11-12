#!/usr/bin/python3
# coder : Himanshu Mishra
# about : reverse string
# algorithm used : simple python builtin function
# links : Text/reverse_string.py

# this fucntion reverse the input string
def main():
    info = '''
    Program : Reverse String

    Reverse the input the string
    '''
    print(info)

    astring = input("Enter text : ")
    alist = list(astring)
    alist.reverse()
    
    print("Reversed Text : ","".join(alist))

# this is the standard biolerplate that calls the main() function.
if __name__ == '__main__':
    main()