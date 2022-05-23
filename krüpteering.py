import easygui as gui

#See programm on mõeldud sõnade krüpteerimiseks.
#Programm küsib, mis krüpteeringut soovid ja mis sõne.
#Programm tagastab krüpteeritud sõnumi


tahestik = " abcdefghijklmnopqrsšzžtuvwõäöüxy"
telefon = [" ","abcä","def","ghi","jkl","mnoõö","pqrs","tuvü","wxyz"]

#Funktsioon, mis muudab tähe vastavaks numbriks, mis kohal ta tähestikus on.
def tahed(sone):
    lopp = []
    for taht in sone:
        if taht.lower() in tahestik:
            lopp.append(str(tahestik.index(taht)))
        else:
            pass
    return " ".join(lopp)

#Funktsioon, mis krüpteeerib sõne caesar'i krüpteeringu järgi.
#Caesar'i krüpteering võtab 3 kohta eespool oleva tähe ja asendab sellega.
def caesar(sone):
    lopp = []
    c_tahestik = tahestik[1:]
    for täht in sone:
        if täht in c_tahestik:
            asd = c_tahestik.index(täht)
            lopp.append(c_tahestik[asd + 3 - len(c_tahestik)])
        else:
            lopp.append(täht)
    return "".join(lopp)

#Programm väljastab
def nuputelefon(sone):
    lopp = []
    for täht in sone:
        for number in range(len(telefon)):
            if täht in telefon[number]:
                lopp.append(str(number + 1) * (telefon[number].index(täht) + 1))
    return " ".join(lopp)


#Programm küsib, mis krüpteerinut kasutaja soovib ja vastavat sõne.
while True:
    valikud = ["Täht numbriks", "Caesar", "Nuputelefon", "Lahku"]
    valik = gui.buttonbox("Mis krüpteeringut soovite?",choices=valikud)

    if valik == "Lahku": #Lahkumisel lõhub while True tsükli ära.
        break

    elif valik == "Täht numbriks":
        sone = gui.enterbox("Sisesta krüpteeritav tekst")
        gui.msgbox(sone + "\n" + tahed(sone), ok_button="Tagasi")

    elif valik == "Caesar":
        sone = gui.enterbox("Sisesta krüpteeritav tekst")
        gui.msgbox(sone + "\n" + caesar(sone), ok_button="Tagasi")

    elif valik == "Nuputelefon":
        sone = gui.enterbox("Sisesta krüpteeritav tekst")
        gui.msgbox(sone + "\n" + nuputelefon(sone), ok_button="Tagasi")
