import hashlib

correct_flag = "utflag{utctf_uses_svg_to_its_fullest}"
correct_flag_hash = hashlib.sha256(correct_flag.encode()).hexdigest()
print(correct_flag_hash)
