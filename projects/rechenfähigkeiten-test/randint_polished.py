# Importiert die Funktion randint aus dem Modul random, um Zufallszahlen zu generieren
# Modul: Eine Datei die Pyhton-Definitionen und -Anweisungen enthält ~ Bibliothek, math und randint
# Import-Befehl: wird verwendet, um auf Funktionen, Klassen und Variablen aus Modulen zuzgreifen
from random import randint

# Programmstart
print('Teste deine Kopfrechenfähigkeiten!')

# Initialisierung (Zuweisung) der Variablen
maximum = 20      # Obergrenze für die Zufallszahlen
genug = False     # Variable, um zu überprüfen, ob der Benutzer aufhören möchte
richtig = True    # Variable, um zu überprüfen, ob die letzte Antwort richtig war
richtige_antworten = 0  # Zähler für richtige Antworten

# Haupt-Schleife des Programms
while richtig and (not genug):
    # Frage an den Benutzer, ob er weitermachen möchte
    print("Noch ein Test?")
    antwort = input("Antwort (j/n): ")

    if antwort == "j":
        # Generierung zweier Zufallszahlen
        zahl1 = randint(1, maximum)
        zahl2 = randint(1, maximum)
        produkt = zahl1 * zahl2  # Berechnung des Produkts der beiden Zahlen

        # Ausgabe der Multiplikationsaufgabe
        print(zahl1, " * ", zahl2)

        # Benutzer gibt das Ergebnis ein
        ergebnis = int(input("Ergebnis: "))

        # Überprüfung, ob die Antwort richtig ist
        if ergebnis == produkt:
            print("richtig!")
            richtige_antworten += 1  # Erhöhe den Zähler bei einer richtigen Antwort
        else:
            print("falsch!")
            richtig = False  # Setze richtig auf False, da die Antwort falsch war
    else:
        genug = True  # Beende das Spiel, wenn der Benutzer 'n' auswählt

# Ausgabe der Gesamtanzahl der richtigen Antworten
print("Anzahl richtiger Antworten:", richtige_antworten)