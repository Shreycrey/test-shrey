import hashlib

correct_flag = "utflag{oh_no_it_didnt_work_</3_i_guess_i_can_just_use_standard_libraries_in_the_future}"
correct_flag_hash = hashlib.sha256(correct_flag.encode()).hexdigest()
print(correct_flag_hash)
