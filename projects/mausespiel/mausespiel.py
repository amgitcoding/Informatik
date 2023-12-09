# Beispielwerte für j, e, a
j, e, a = 10, 15, 20

# Test der logischen Ausdrücke
print("j liegt zwischen e und a:", (e < j < a) or (a < j < e))
print("j, e und a sind alle verschieden:", (j != e) and (j != a) and (e != a))
print("a ist nicht die kleinste Zahl:", (j < a) or (e < a))
print("Mindestens zwei Anzahlen sind gleich groß:", (j == e) or (j == a) or (e == a))
print("Genau zwei Anzahlen sind gleich groß:", ((j == e) and (j != a)) or ((j == a) and (j != e)))