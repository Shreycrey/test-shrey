#!/usr/bin/exec-suid -- /usr/bin/python3

import hashlib
import os
import sys

# SHA-256 hash of the correct flag (precomputed)
correct_flag_hash = "1e836b225ec5519b22eb7487f9138d4ff0924a772124da895f29e0e625ee1456" 

def get_user_flag():
    return input("Enter the flag: ").strip()

def verify_flag(user_flag):
    # Compute SHA-256 hash of the user-provided flag
    user_flag_hash = hashlib.sha256(user_flag.encode()).hexdigest()
    return user_flag_hash == correct_flag_hash

def read_flag_file():
    with open('/flag', 'r') as f:
        return f.read()

def main():
    user_flag = get_user_flag()
    if verify_flag(user_flag):
        print("Correct flag!")
        print(read_flag_file())
    else:
        print("Incorrect flag.")

if __name__ == '__main__':
    main()

