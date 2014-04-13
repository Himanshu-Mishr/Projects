"""
Program to convert binary to decimal , vice-versa
"""

q = ['2','3','4','5','6','7','8','9']

def toBin(num):
    return bin(int(str(num)))[2:]

def toDeci(num):
    if [ True for i in list(str(num)) if i in q ]: return num
    else: return str(int(str(num),2))

