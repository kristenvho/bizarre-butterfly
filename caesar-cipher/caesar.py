# -*- coding: UTF-8 -*-

# caesar.py
#  Encrypts and decrypts text using Caesar cipher.

import getopt, sys

# Ciphering function
def cipher(mode, message):
# Encrypting the message
#    if mode == 'encrypt':
        
# Decrypting the message
#    else:
        
    return message
    
def main(argv):
    # Variables
    mode = 'decrypt'
    key = 13

    # Identify flags and arguments
    try:
	    opts, args = getopt.getopt(argv, "edk:", ["encrypt", "encipher", "decrypt", "decipher", "key="])
    except getopt.GetoptError:
        print "Usage: caesar.py [-e, --encrypt, --encipher] [-d, --decrypt, --decipher]"
        print "[-k(1..26), -key=(1..26)] \"message\""
        print "Without flags, will default to ROT13 decryption."
        sys.exit(2)

    for opt, arg in opts:
        
        if opt in ("-e", "--encrypt", "--encipher"):
            mode = 'encrypt'
        elif opt in ("-d", "--decrypt", "--decipher"):
            mode = 'decrypt'
        elif opt in ("-k", "--key"):
            key = arg
        else:
            print "Usage: caesar.py [-e, --encrypt, --encipher] [-d, --decrypt, --decipher]"
            print "[-k(1..26), -key=(1..26)] \"message\""
            print "Without flags, will default to ROT13 decryption."
            sys.exit(2)

    # Get message
    message = "".join(args)
    
    # Decipher/encipher the message
    cipherMessage = cipher(mode, message)
    
    # Print ciphered message
    print "Mode: " + mode + "\t\tKey: " + str(key)
    print cipherMessage
	
    sys.exit(0)

if __name__ == "__main__":
    main(sys.argv[1:])

    
