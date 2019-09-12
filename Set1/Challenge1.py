#!/usr/bin/python

def convertToHex ( input ):
    base64 = input.decode("hex").encode("base64")
    print('\n' + base64)


input = raw_input("Please enter the hex to encode: ")
convertToHex(input)
