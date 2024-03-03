# Dieses Programm zeigt Beispiele für bedingte Anweisungen und für Schleifen

# Einfache if-Bedingung
inp=float(input("Bitte eine Zahl eingeben"))
if inp>0:
    print("Der eingegebene Wert ist größer als 0.")
    # Alle Anweisungen hinter der if-Zeile, die eingerückt sind, werden nur bei erfüllter if-Bedingung durchlaufen
print("Hier sind wir wieder im unbedingten Teil des Programms.")

# if-Bedingung mit elif und else
if inp>10:
    print("Der eingegebene Wert ist größer als 10.")
    # Alle Anweisungen hinter der if-Zeile, die eingerückt sind, werden nur bei erfüllter if-Bedingung durchlaufen
elif inp>0:
    print("Der eingegebene Wert ist größer als 0 aber kleiner als 10.")
elif inp==0:
    print("Der eingegebene Wert ist gleich 0.")
else:
    print("Der eingegebene Wert ist kleiner als 0.")
print("Hier sind wir jetzt wieder im unbedingten Teil des Programms.")

#Einfache while-Schleife
print("while-Schleife zum Runterzählen von 10 bis 1")
n=10
while n>0:
    print("n=",n)
    n=n-1 #Man kann stattdessen auch n-=1 schreiben

#while-Schleife mit break zum Abbrechen
print("Diese while-Schleife zählt hoch bis 10")
while 1==1:
    print("n=",n)
    n=n+1 
    if n>10:
        break

#Einfache for-Schleife
print("Jetzt zählen wir mit einer for-Schleife hoch bis 5")
for n in range(1,6): #Wenn man nur range(6) schreibt, dann startet der Bereich bei 0. 
    print("n=",n)

#for-Schleife mit einem Range-Step von -2
print("Nun zählen wir mit einer for-Schleife in zweierschritten von 10 runter")
for n in range(10,1,-2): 
    print("n=",n)

#for-Schleife über alle Elemente einer Liste
meineListe = (1,1,2,3,5,8,13)
print("Und jetzt gehen wir mit for-Schleife durch eine Liste")
print("   Die Fibonacci-Folge beginnt mit: ", end="")
for elem in meineListe:
    print(elem, " ",end="")
    #Sollte man die for-Schleife vorzeitig verlassen wollen, dann geht das mit "break"
print()
print("Die Schleifenvariable elem hat nach der Schleife den Wert:", elem)
#Ein Beispiel für eine for-Schleife über die Elemente eines Dictionaries hatten wir bereits in print_examples.py