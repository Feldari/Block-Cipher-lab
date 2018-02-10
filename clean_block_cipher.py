#!/usr/bin/env python3.6

def key():
    '''
    Block of code to define the encryption key
    '''
    keyout = []
    keyin = ''

    userin = input('\nEnter your text key: ').upper()

    # collapse string and sort the key alphabetically
    keyin = collapse(userin)
    sortin = sorted(keyin)

    # remove spaces and non-letters fom key
    for lett in sortin:
        keyout.append(keyin.index(lett))
        keyin = keyin.replace(lett, '.',1)

    # return key as list
    return keyout

def collapse(userin):
    '''
    This collapses a string to just capital A - Z
    '''
    strout = ''
    for lett in userin:
        if (ord(lett) < 65) | (ord(lett) > 90):
            pass
        else:
            strout += lett
    
    return strout

def pad(nospace, keyout):
    '''
    add random padding to end of string if its legnth does not match key
    '''
    while (len(nospace) % len(keyout)) != 0:
        nospace += (chr(random.randint(65, 90)))
    return nospace

def encode(keyout):
    '''
    Key should be list of random non repeating numbers from 0 - len(key)-1 
    import random required to make this work
    '''
    original = input('\nEnter text string to encode: ').upper()

    # collapse string and pad legnth
    nospace = collapse(original)
    padded = pad(nospace, keyout) 
    
    # Encoding block take legnth of key worth of plaintext to process
    # remove letters processed and repeat
    final = ''
    while padded != '':
       for num in range(len(keyout)):
            final += padded[keyout[num]]
       padded = padded[len(keyout):]
    
    return final

def decode(keyout):
    '''
    Key should be list of random non repeating numbers from 0 - len(key)-1 
    import random required to make this work
    '''
    original = input('\nEnter text string to decode: ').upper()

    # colapse string and pad legnth
    nospace = collapse(original)
    padded = pad(nospace, keyout)

    # Encoding block take legnth of key worth of plaintext to process
    # remove letters processed and repeat
    final = ''
    while padded != '':
       for num in range(len(keyout)):
            final += padded[keyout.index(num)]
       padded = padded[len(keyout):]
    
    return final

def menu():
    exit = 0
    while exit != 1:
        print('What would you like to do?')
        print('1. Encode')
        print('2. Decode')
        print('3. Exit')
        option = input('>>').upper()
        
        if  option == 'ENCODE' or option == '1':
            print()
            keyout = key()
            print('\nYour encoded string:\n', encode(keyout), '\n\n', sep='')

        elif option == 'DECODE' or option == '2':
            print()
            keyout = key()
            print('\nYour decoded string:\n', decode(keyout), '\n\n', sep='')

        elif option == 'EXIT' or option == '3':
            exit = 1

        else:
            print('Please enter a valid option!')

if __name__ == '__main__':

    import random

    menu()

