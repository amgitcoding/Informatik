# Eingabe der Werte durch den Benutzer
j = int(input("Anzahl der jungen Mäuse (j): "))
e = int(input("Anzahl der erwachsenen Mäuse (e): "))
a = int(input("Anzahl der alten Mäuse (a): "))

# Test der logischen Ausdrücke mit if-else-Bedingungen
if (e < j < a) or (a < j < e):
    print("j liegt zwischen e und a.")
else:
    print("j liegt nicht zwischen e und a.")

if (j != e) and (j != a) and (e != a):
    print("j, e und a sind alle verschieden.")
else:
    print("j, e und a sind nicht alle verschieden.")

if (j < a) or (e < a):
    print("a ist nicht die kleinste Zahl.")
else:
    print("a ist die kleinste Zahl.")

if (j == e) or (j == a) or (e == a):
    print("Mindestens zwei Anzahlen sind gleich groß.")
else:
    print("Keine zwei Anzahlen sind gleich groß.")

if ((j == e) and (j != a)) or ((j == a) and (j != e)) or ((e == a) and (e != j)):
    print("Genau zwei Anzahlen sind gleich groß.")
else:
    print("Entweder sind alle Anzahlen verschieden oder alle gleich.")