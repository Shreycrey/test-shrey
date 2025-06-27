import subprocess
import re
from Crypto.Cipher import DES

responses = []

CK_A = bytes.fromhex("dae55498c4325458")
CK_B = bytes.fromhex("26fb153885bcb06b")
cipher_A = DES.new(CK_A, DES.MODE_ECB)
cipher_B = DES.new(CK_B, DES.MODE_ECB)


def luhn_check(cardNb):
    cardNb = str(cardNb)
    nDigits = len(cardNb)
    total = 0
    alt = False
    for i in range(nDigits - 1, -1, -1):
        d = int(cardNb[i])
        if alt:
            d *= 2
            if d > 9:
                d -= 9
        total += d
        alt = not alt
    return total % 10 == 0

def generate_cvv(PAN, date, code):
    key = (PAN + date + code).ljust(32, '0')
    f_half = key[:16]
    s_half = key[16:]
    step1 = cipher_A.encrypt(bytes.fromhex(f_half))
    step2 = bytes(a ^ b for a, b in zip(step1, bytes.fromhex(s_half)))
    step3 = cipher_A.encrypt(step2)
    step4 = cipher_B.decrypt(step3)
    step5 = cipher_A.encrypt(step4)
    result = "".join(i for i in step5.hex() if i.isdigit())[:3]
    return result

def solve():
    p = subprocess.Popen(
        ["python3", "server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    PAN = date = code = cvv = None

    for line in p.stdout:
        print(line, end='')

        if "PAN:" in line:
            parts = line.strip().split(", ")
            PAN = parts[0].split(": ")[1]
            date = parts[1].split(": ")[1]
            code = parts[2].split(": ")[1]
            cvv = parts[3].split(": ")[1]

        if "Valid?" in line:
            if luhn_check(PAN) and generate_cvv(PAN, date, code) == cvv:
                answer = "1"
            else:
                answer = "0"
            p.stdin.write(answer + "\n")
            p.stdin.flush()
            responses.append(answer)

    print("\nFinal Collected Bits:", "".join(responses))

if __name__ == "__main__":
    solve()

