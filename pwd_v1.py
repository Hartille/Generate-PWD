import random

def gen_pwd():
    consonne = "bcdfghjklmnpqrstvwxz"
    voyelle = "aeiouy"
    special = "%$*+&=@!"
    chiffre = "0123456789"
    
    ch1 = random.choice(consonne)
    ch2 = random.choice(voyelle).upper()
    ch3 = random.choice(consonne)
    ch4 = random.choice(special)
    ch5 = random.choice(chiffre)
    ch6 = random.choice(voyelle)
    ch7 = random.choice(consonne).upper()
    ch8 = random.choice(voyelle)
    ch9 = random.choice(special)
    ch10 = random.choice(chiffre)

    pwd = ch1 + ch2 + ch3 + ch4 + ch5 + ch6 + ch7 + ch8 + ch9 + ch10
    return pwd

print(gen_pwd())