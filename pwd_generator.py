import random
import string

def gen_password(min_length,num=True,spl_char=True):
    letters=string.ascii_letters
    digits=string.digits
    spl=string.punctuation

    characters=letters
    if num:
        characters+=digits
    if spl_char:
        characters+=spl

    pwd=""
    flag=False
    has_num=False
    has_spl=False

    while not flag or len(pwd)<min_length:
        new_char=random.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_num=True
        elif new_char in spl:
            has_spl=True

        flag=True;

        if num:
            flag= has_num
        if spl_char:
            flag=flag and has_spl
    
    return pwd


min_length=int(input("Enter the minimun length of password: "))
has_num=input("Do you want digits?(y/n) ").lower() =="y"
has_spl=input("Do you want special characters?(y/n) ").lower() =="y"
pwd=gen_password(min_length,has_num,has_spl)
print(pwd)



