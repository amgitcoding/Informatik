def Schaltjahr(jahr):
    while jahr > 0:
        if jahr % 4 == 0:
            if jahr % 100 == 0 and jahr % 400 != 0:
                print(jahr, "ist kein Schaltjahr")
                return False
            else:
                print(jahr, "ist ein Schaltjahr")
                return True
        else: 
            print(jahr, "ist kein Schaltjahr")
            return False
         
jahr = int(input("Bitte geben Sie das Jahr ein: "))

Schaltjahr(jahr)