# variable ist_schaltjahr nimmt ein Jahr als Argument 
# und gibt True zurück, wenn es ein Schaltjahr ist, sonst False.

def ist_schaltjahr(jahr):
    if (jahr % 400 == 0) or (jahr % 4 == 0 and jahr % 100 != 0):
        return True
    else:
        return False

# while-Schleife läuft kontinuierlich, bis der Benutzer
# sie mit einer bestimmten Eingabe (z. B. “exit”) beendet.
# mit try und except wird die handhabung von 
# nicht-numerischen zahlen ermöglicht.
# Nutzung von f-string

while True:
    try:
        jahr = int(input("Jahr (oder 'exit' zum Beenden): "))
        if ist_schaltjahr(jahr):
            print(f"{jahr} ist ein Schaltjahr.")
        else:
            print(f"{jahr} ist kein Schaltjahr.")
    except ValueError:  # Abfangen von nicht-integer Eingaben
        print("Programm beendet.")
        break

def finde_schaltjahre(startjahr, endjahr):
    # Gibt eine Liste aller Schaltjahre zwischen startjahr und endjahr zurück.
    # + 1 um endjahr auch mit einzubeziehen
    return [jahr for jahr in range(startjahr, endjahr + 1) if ist_schaltjahr(jahr)]
 
while True:
    eingabe = input("Startjahr (oder 'exit' zum Beenden): ")
    # Anwendung von .lower Methode um alle Schreibweisen von 'exit' zu ignorieren
    if eingabe.lower() == 'exit':
        print("Programm beendet.")
        break

    try:
        startjahr = int(eingabe)
        endjahr = int(input("Endjahr: "))

        if startjahr > endjahr:
            print("Das Startjahr muss vor dem Endjahr liegen.")
            continue

        schaltjahre = finde_schaltjahre(startjahr, endjahr)
        if schaltjahre:
            print(f"Schaltjahre zwischen {startjahr} und {endjahr}: {schaltjahre}")
        else:
            print(f"Es gibt keine Schaltjahre zwischen {startjahr} und {endjahr}.")

    except ValueError:
        print("Bitte geben Sie eine gültige Jahreszahl ein.")