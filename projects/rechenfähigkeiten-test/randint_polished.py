from random import randint

print('Teste deine Kopfrechenfähigkeiten!')
maximum = 20
genug = False
richtig = True
richtige_antworten = 0  # Zähler für richtige Antworten

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
            richtige_antworten += 1  # Erhöhe den Zähler
        else:
            print("falsch!")
            richtig = False
    else:
        genug = True

print("Anzahl richtiger Antworten:", richtige_antworten)