#! /usr/local/bin/python3

#infinite chill / 2017

import sys
import csv
import uuid
import hashlib

def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    hashed_password=hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    return hashed_password
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()


def main():
    #print greeting
    print ("\nbcrypt password tool 1.0")

    while (1):
        print("\n(n)ew, (v)erify, (q)uit")
        todo=input("what would you like to do : ")
        if todo == 'n':
            todo=input("enter password : ")
            hashed_password=hash_password(todo)
            print("sha256: ", hashed_password)
        elif todo == 'v':
            plain_text_password=input("enter plain text password to check: ")
            verify = check_password(hashed_password,plain_text_password)
            if(verify):
                print("match")
            else:
                print("no match")
        elif  todo == 'q':
            break
        else:
            pass

main()