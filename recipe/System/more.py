#!/usr/bin/python3
"""
 Coder : Himanshu Mishra (himanshu.m786@gmail.com)
 About : split and interactively page a string or file of text
 Justify Location : system/more.py
 Link : 79
"""

"""
this function takes input as text and print 15 lines at a time.
And at the end of each print it ask to print more .....
"""
def more(text,numlines=15):
    lines = text.splitlines()  # like split ('\n') but no '' at end
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk:print(line)
        if lines and input("More?") not in ['y','Y']:break



if __name__ == '__main__':
    import sys
    more(open(sys.argv[1]).read(),10)
