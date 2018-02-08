#!/usr/bin/env python3.6

def key():

    '''
    Block of code to define the encryption key
    '''
    keyout = []
    keyin = ''

    userin = input('\nEnter your text key: ').upper()
    # swap comments between above and below for debugging and live
    # userin = 'test string'.upper()

    # colapse and filter user supplied key
    for lett in userin:
        if (ord(lett) < 65) | (ord(lett) > 90):
            pass
        else:
            keyin += lett

    # sort the proposed key alphabetically
    sortin = sorted(keyin)

    # remove spaces and non-letters fom key
    for lett in sortin:
        keyout.append(keyin.index(lett))
        keyin = keyin.replace(lett, '.',1)

    # return key as list
    return keyout

def encode(key):
    '''
    Block of code to encode your message
    key should be a randomly ordered list of numbers which contain numbers from 
    0 to len(key)-1

    import random required to make this work
    '''
    original = input('\nEnter text string to encode: ').upper()
    # swap comments on above and below line to finish or debug program
    # original = 'big long test string to encode as test string'.upper()

    nospace = '' 
    # remove spaces and non-letters from encoding string put string into list
    for lett in original:
        if (ord(lett) < 65) | (ord(lett) > 90):
            pass
        else:
            nospace += lett
    
    # add random letters to end of plaintext to 
    # make plaintext block match key size
    while (len(nospace) % len(key)) != 0:
        nospace += (chr(random.randint(65, 90)))
    
    # Encoding block take legnth of key worth of plaintext to process
    # remove letters processed and repeat
    final = ''
    while nospace != '':
       for num in range(len(key)):
            final += nospace[key[num]]
       nospace = nospace[len(key):]
    
    return final

def decode(key):
    '''
    Block of code to encode your message
    key should be a randomly ordered list of numbers which contain numbers from 
    0 to len(key)-1

    import random required to make this work
    '''
    original = input('\nEnter text string to decode: ').upper()
    # swap comments on above and below line to finish or debug program
    # original = 'big long test string to encode as test string'.upper()
    # original = encode(key)

    nospace = '' 
    # remove spaces and non-letters from encoding string put string into list
    for lett in original:
        if (ord(lett) < 65) | (ord(lett) > 90):
            pass
        else:
            nospace += lett
    
    # add random letters to end of plaintext to 
    # make plaintext block match key size
    while (len(nospace) % len(key)) != 0:
        nospace += (chr(random.randint(65, 90)))
    
    # Encoding block take legnth of key worth of plaintext to process
    # remove letters processed and repeat
    final = ''
    while nospace != '':
       for num in range(len(key)):
            final += nospace[key.index(num)]
       nospace = nospace[len(key):]
    
    return final
if __name__ == '__main__':

    import random

    exit = 0
    while exit != 1:
        print('What would you like to do?')
        print('1. Encode')
        print('2. Decode')
        print('3. Exit')
        option = input('>>').upper()
        
        if  option == 'ENCODE' or option == '1':
            print('\nYour encoded string:\n', encode(key()), '\n\n', sep='')

        elif option == 'DECODE' or option == '2':
            print('\nYour decoded string:\n', decode(key()), '\n\n', sep='')

        elif option == 'EXIT' or option == '3':
            exit = 1

        else:
            print('Please enter a valid option!')

