Name = "Aidan"
print("Aidan ist mein Name")
print(f"{Name} ist mein Name")


for n in range(1,6):
    print("n: ",n)

nachname, vorname = input("Bitte Name und Vorname eingeben (getrennt durch Komma)").split()

a = (2*3)
print("Der Wert von a ist: ",a)


befinden_abfrage = True
schüler = ["Felix", "Tom", "Aidan", "Niclas"]
inp_name = input("Was ist dein Name? ")

for s in schüler:
    if s == inp_name:
        print("Du befindest dich bereits in der Krusliste! ")
    else:
        while befinden_abfrage == True:
            print("Du befindest dich noch nicht in der Kursliste! ")
            inp_interesse = input("Möchtest du der AG Data Sience beitreten? (Ja/Nein) ")
            if inp_interesse == "Ja":
                print(f"{inp_name}, du bist erfolgreich der AG Data Sience beigetreten! ")
                befinden_abfrage = False
            elif inp_name == "Nein":
                print("Schade! Dann bis bald!")
                befinden_abfrage = False
            else:
                print("Versuchen Sie es erneut.")
