from random import randint

print('Teste deine Kopfrechenfähigkeiten!')
maximum = 20
genug = False
richtig = True
while richtig and (not genug):
    print("Noch ein Test?")
    antwort = input("Antwort (j/n): ")
    if antwort == "j":
        zahl1 = randint(1, maximum)
        zahl2 = randint(1, maximum)
        produkt = zahl1 * zahl2
        print(zahl1, " * ", zahl2)
        ergebnis = int(input("Ergebnis: "))
        if ergebnis == produkt:
            print("richtig!")
        else:
            print("falsch!")
            richtig = False
    else:
        genug = True