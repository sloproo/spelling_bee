import string

def syotto() -> tuple[str, str]:
    while True:
        pakollinen = input("Mikä kirjain on keskellä?:\n\t")
        if len(pakollinen) != 1 or pakollinen not in string.ascii_lowercase:
            print("\nAnna vain yksi pieni kirjain :|\n")
            continue
        break
    while True:
        muut = input("Mitkä ovat muut kirjaimet?:\n\t")
        if len(set(muut)) != 6 or len(muut) != 6:
            print("\nKuutta pientä eri kirjainta yhdessä möykyssä haetaan :|\n")
            continue
        for s in muut:
            if s not in string.ascii_lowercase:
                print("\nAnna vain pieniä kirjaimia :|\n")
                break
            if s == pakollinen:
                print(f"\n{pakollinen} on jo kukan keskellä oleva kirjain :|\n")
        else:
            break
    return ((pakollinen, muut + pakollinen))

pakollinen, kaikki = syotto()
kelvolliset = []
with open("words_trimmed.txt") as f:
    for sana in f:
        sana = sana.strip()
        if sana == "biotech":
            pass
        if pakollinen not in sana:
            continue
        for c in set(sana):
            if c not in kaikki:
                break
        else:
            kelvolliset.append(sana)

kelvolliset.sort(key=lambda sana: len(sana))

i = 0
for kelpo in kelvolliset:
    print(kelpo, end="\t\t\t")
    i += 1
    if i % 4 == 0:
        print()
