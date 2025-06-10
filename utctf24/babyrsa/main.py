#!/usr/bin/exec-suid -- /usr/bin/python3 -I

from Crypto.Util.number import long_to_bytes
import sys

def read_vals():
    with open("vals.txt", "r") as f:
        lines = f.read().strip().split("\n")
        N = int(lines[0].split("=")[1].strip())
        e = int(lines[1].split("=")[1].strip())
        c = int(lines[2].split("=")[1].strip())
    return N, e, c

def get_real_flag():
    try:
        with open("/flag", "r") as f:
            return f.read().strip().encode()
    except:
        print("Error: Cannot read flag.", file=sys.stderr)
        exit(1)

def main():
    print("RSA-256 Challenge")
    N, e, c = read_vals()
    print("Please decrypt the ciphertext and enter the plaintext integer (m):")
    
    try:
        m = int(input("m = ").strip())
        m_bytes = long_to_bytes(m)
        real_flag = get_real_flag()

        if m_bytes == real_flag:
            print(real_flag.decode())  # Print the actual flag
        else:
    except Exception as e:
        print("Invalid input or error:", e, file=sys.stderr)

if __name__ == "__main__":
    main()
