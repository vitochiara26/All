import random as rng


aminoacidos = ["Ala", "Arg", "Asn", "Asp", "Cys", "Gln", "Glu", "Gly", "His", "Ile", 
                "Leu", "Lys", "Met", "Phe", "Pro", "Ser", "Thr", "Trp", "Tyr", "Val"]

cadena_prot = ""

for _ in range(199):
    cadena_prot += f"{rng.choice(aminoacidos)}-";
cadena_prot += f"{rng.choice(aminoacidos)}";

print(cadena_prot)
