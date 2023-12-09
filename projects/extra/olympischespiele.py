jahr = int(input('Jahr: '))

# Verarbeitung und Ausgabe
if (jahr % 4 == 0 and jahr > 1896 and jahr != 2020) or jahr == 2021:
    warenOlympischeSpiele = True
else:
    warenOlympischeSpiele = False

# Ausgabe
if warenOlympischeSpiele == True:
    print(jahr, 'fanden olympische Spiele statt.')
else:
    print(jahr, 'fanden keine olympische Spiele statt.')


jahr = int(input('Jahr: '))

# Erstelle eine Liste der Jahre, in denen Olympische Spiele stattfanden
olympische_jahre = [i for i in range(1896, 2021, 4) if i != 1940 and i != 1944 and i != 2020]
olympische_jahre.append(2021) # Füge das Jahr 2021 hinzu, da die Spiele von 2020 verschoben wurden

# Überprüfe, ob das Jahr in der Liste ist
warenOlympischeSpiele = jahr in olympische_jahre

# Ausgabe
if warenOlympischeSpiele:
    print(jahr, 'fanden olympische Spiele statt.')
    
else:
    print(jahr, 'fanden keine olympische Spiele statt.')