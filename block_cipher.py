#!/usr/bin/env python3.6

def key():

    '''
    Block of code to define the encryption key
    '''
    keyout = []

    # keyin = input('Enter your text key: ').upper()
    # swap comments between above and below for debugging and live
    keyin = 'test string'.upper()

    # sort the proposed key alphabetically
    sortin = sorted(keyin)

    # remove spaces and non-letters fom key
    for lett in sortin:
        if (ord(lett) < 65) | (ord(lett) > 90):
            pass
        else:
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
    # original = input('enter text string to encode: ').upper()
    # swap comments on above and below line to finish or debug program
    original = 'big long test string to encode as test string'.upper()

    nospace = []

    # remove spaces and non-letters from encoding string
    for lett in original:
        if (ord(lett) < 65) | (ord(lett) > 90):
            pass
        else:
            nospace.append(lett)

    # add random letters to end of plaintext to 
    # make plaintext block match key size
    while (len(nospace) % len(key)) != 0:
        nospace.append(chr(random.randint(65, 90)))

    ##################################################
    # i have a list ready for encoding i just need to figure out how to
    # break the list into the consituant blocks. maybe i can use list 
    # slicing [0:len(nospace)] or some such nonsense
    ##################################################
    final = ''
    for char in key:
        x = int(char)
        final = final + nospace[x]


    print(nospace)
    print(key)
    print(final)


if __name__ == '__main__':

    import random

    key = key()        
    encode(key)

