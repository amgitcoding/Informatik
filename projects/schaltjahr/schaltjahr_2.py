# variable ist_schaltjahr nimmt ein Jahr als Argument 
# und gibt True zurück, wenn es ein Schaltjahr ist, sonst False.

def ist_schaltjahr(jahr):
    # Prüft, ob das gegebene Jahr ein Schaltjahr ist.
    return (jahr % 400 == 0) or (jahr % 4 == 0 and jahr % 100 != 0)

def finde_schaltjahre(startjahr, endjahr):
    # Gibt eine Liste aller Schaltjahre zwischen startjahr und endjahr zurück.
    # + 1 um endjahr auch mit einzubeziehen
    return [jahr for jahr in range(startjahr, endjahr + 1) if ist_schaltjahr(jahr)]

def menue_anzeigen():
    # Zeigt das Hauptmenü des Programms an.
    print("\nSchaltjahr-Programm")
    print("1. Überprüfen, ob ein bestimmtes Jahr ein Schaltjahr ist")
    print("2. Alle Schaltjahre in einem Zeitraum finden")
    print("3. Programm beenden")

def hauptmenue():
    while True:
        menue_anzeigen()
        auswahl = input("Wählen Sie eine Option (1, 2, 3): ")

        if auswahl == "1":
            jahr = int(input("Bitte geben Sie ein Jahr ein: "))
            if ist_schaltjahr(jahr):
                print(f"{jahr} ist ein Schaltjahr.")
            else:
                print(f"{jahr} ist kein Schaltjahr.")
        elif auswahl == "2":
            startjahr = int(input("Startjahr: "))
            endjahr = int(input("Endjahr: "))
            
            if startjahr > endjahr:
                print("Das Startjahr muss vor dem Endjahr liegen.")
                continue
        
            schaltjahre = finde_schaltjahre(startjahr, endjahr)
            if schaltjahre:
                print(f"\nSchaltjahre zwischen {startjahr} und {endjahr}: {schaltjahre}")
            else:
                print(f"\nEs gibt keine Schaltjahre zwischen {startjahr} und {endjahr}.")
        elif auswahl == "3":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

# Hauptprogramm starten
hauptmenue()
