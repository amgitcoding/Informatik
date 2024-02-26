n = 4
def Fakultät(n):
    if n < 2:
        return 1
    else:
        return n * Fakultät(n - 1)
       

a = input("Für welche Zahl soll die Fakultät berechnet werden? ")
a = int(float(a))
print(a, "! = ", Fakultät(a), sep="")
