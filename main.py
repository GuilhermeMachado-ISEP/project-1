from encrypt import encrypt

def main():
    print('Welcome to the CypherCLI main interface, please input a String to be encrypted')

    s = input('String to input')

    encrypt(s)


main()