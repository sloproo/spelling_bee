with open("words_alpha.txt") as f:
    trimmattu = []
    i = 0
    for r in f:
        if i % 10000 == 0:
            print(f"sana nro {i}, sana {r}")
        if len(r) >= 5:
            trimmattu.append(r.strip())
        i += 1

with open("words_trimmed.txt", "a") as f:
    f.write("\n".join(trimmattu))


