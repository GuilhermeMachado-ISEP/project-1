from encrypt import encrypt

def main():
    print('Welcome to the CypherCLI main interface, please input a String to be encrypted')

    s = encrypt(input('Enter a String: '))

    print('Encrypted String: ', s)


main()