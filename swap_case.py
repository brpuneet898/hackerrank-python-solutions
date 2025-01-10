# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    f = ""
    for i in s:
        if i.islower():
            f = f + i.upper()
        elif i.isupper():
            f = f + i.lower()
        else:
            f = f + i
    return f