from encrypt import encrypt
from decrypt import decrypt

def main():
    print('Welcome to the CypherCLI main interface, please input a String to be encrypted')

    s = encrypt(input('Enter a String: '))

    print('Encrypted String: ', s)

    s = decrypt(s)

    print('Decrypted String: ', s)

main()