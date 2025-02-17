import random

def gen_pwd():
    consonne = "bcdfghjklmnpqrstvwxz"
    voyelle = "aeiouy"
    special = "%$*+&=@!"
    chiffre = "0123456789"
    
    ch1 = random.choice(chiffre)
    ch2 = random.choice(chiffre)
    ch3 = random.choice(chiffre)
    ch4 = random.choice(chiffre)
    ch5 = random.choice(voyelle).upper()
    ch6 = random.choice(consonne)
    ch7 = random.choice(voyelle)
    ch8 = random.choice(consonne)
    ch9 = random.choice(voyelle)
    ch10 = random.choice(consonne)
    ch11 = random.choice(special)

    pwd = ch1 + ch2 + ch3 + ch4 + ch5 + ch6 + ch7 + ch8 + ch9 + ch10 + ch11
    return pwd

number = int(input("Nombre de mots de passe à générer : "))

file_name = "pwd.txt"

with open(file_name, 'w') as file:
    for _ in range(number):
        pwd = gen_pwd()
        file.write(pwd + "\n")

print(f"{number} mots de passe ont été générés dans le fichier {file_name}")