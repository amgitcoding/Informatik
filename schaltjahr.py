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