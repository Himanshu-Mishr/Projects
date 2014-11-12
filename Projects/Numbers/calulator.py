'''
Calculator
'''
def main():
    print(' \033[1;44mWelcome to myCalculator:\033[1;m')
    print(' \033[1;45mINFO : Ctrl + z to exit \033[1;m')
    while(True):
        try:
            print("\033[1;32m|=", eval(input("|< ")), "\033[1;m")
        except:
            print('\033[1;31mWrong Symbol Input\033[1;m')
if __name__ == '__main__':
    main()
