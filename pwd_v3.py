import random

def gen_pwd(length=20):
    consonnes = "bcdfghjklmnpqrstvwxz"
    consonnes_maj = "BCDFGHJKLMNPQRSTVWXZ"
    voyelles = "aeiouy"
    special = "%$*+&=@!"
    chiffres = "0123456789"
    
    categories = [consonnes, voyelles, special, chiffres, consonnes_maj]
    password = "".join(random.choice(random.choice(categories)) for _ in range(length))
    
    return password

print(gen_pwd())