from encrypt import encrypt
from decrypt import decrypt

def main():
    print('Welcome to the CypherCLI main interface, please make a choice between one of the options below')

    print('1: Just Encrypt')

    print('2: Just Decrypt')

    print('3: Encrypt, then Decrypt')

    print('0: Exit')

    s = int(input('Enter a option: '))

    while 0 > s > 3:
        print('Invalid option')
        s = int(input('Enter a option: '))

    if s == 1:
        s = encrypt(input('Enter a String: '))
        print('Encrypted String: "', s, '"')
    elif s == 2:
        s = input('Enter a String: ')
        if (int(s[-2]) != 0 and int(s[-2]) != 1) or (int(s[-1]) != 0 and int(s[-1]) != 1):
            print('String was not encrypted by this cypher')
        else:
            s = decrypt(s)
            print(f'Decrypted String: "{s}"')
    elif s == 3:
        s = encrypt(input('Enter a String: '))
        print('Encrypted String: ', s)
        s = decrypt(s)
        print('Decrypted String: ', s)


main()