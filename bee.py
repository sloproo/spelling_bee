def syotto() -> set:
    while True:
        pakollinen = input("Mikä kirjain on keskellä?:\n\t")
        if len(pakollinen) != 1:
            print("\nAnna vain yksi kirjain :|\n")
            continue
        if pakollinen not in kolmoset:
            print("\n Tätä sanaa ei löydy sanastosta. Typo vai Hesarin moka?\n")
            continue
        break
    while True:
        muut = input("Mitkä ovat muut kirjaimet?:\n\t")
        if len(muut) != 5:
            print("\nViittä kirjainta yhdessä möykyssä haetaan :|\n")
            continue
        break
    return (pakollinen, muut)
