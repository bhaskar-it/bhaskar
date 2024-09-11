import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+','=','-']
print(":::::::::::::::-WELLCOME TO PASSWORD GENNETOR-:::::::::::::::::")
no_letters=int(input("enter how many letters do you want in password:"))
no_symbols=int(input("enter how many syboles do you want in password:"))
no_numbers=int(input("enter how many numbers do you want in password:"))
passwor=""
for i in range(1,no_letters+1):
    char=random.choice(letters)
    passwor += char
for i in range(1,no_symbols+1):
    char=random.choice(symbols)
    passwor += char
for i in range(1,no_numbers+1):
    char=random.choice(numbers)
    passwor += char
pas=list(passwor)
l=len(pas)
p=""
for i in range(l):
    char=random.choice(pas)
    p += char
print(f"Your password is:    {p}")
    