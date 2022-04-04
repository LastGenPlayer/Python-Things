täpid = {"Õ":27,"Ä":28,"Ö":29,"Ü":30}
keemias ={"a":18,"b":5,"c":6,"d":66,"e":63,"f":9,"g":31,"h":1,"i":53,"j":53,"k":19,"l":3,"m":12,"n":7,"o":8,"p":15,"q":"6*","r":44,"s":16,"t":22,"u":92,"v":74,"w":74,"x":54,"y":23,"z":40}
telo = [" ","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
tahestik = " abcdefghijklmnopqrsšzžtuvwõäöüxy"
morse = {"a":".-",
         "b":"-...",
         "c":"-.-.",
         "d":"-..",
         "e":".",
         "f":"..-.",
         "g":"--.",
         "h":"....",
         "i":"..",
         "j":".---",
         "k":"-.-",
         "l":".-..",
         "m":"--",
         "n":"-.",
         "o":"---",
         "p":".--.",
         "q":"--.-",
         "r":".-.",
         "s":"...",
         "t":"-",
         "u":"..-",
         "v":"...-",
         "w":".--",
         "x":"-..-",
         "y":"-.--",
         "z":"--..",
         "0":"-----",
         "1":".----",
         "2":"..---",
         "3":"...--",
         "4":"....-",
         "5":".....",
         "6":"-....",
         "7":"--...",
         "8":"---..",
         "9":"----.",
         " ":"/"
         }

corpusL = {"b":"t", "c":"y",
           "d":"p", "f":"t",
           "g":"j", "h":"k",
           "j":"t", "l":"p",
           "m":"s", "n":"t",
           "p":"k", "q":"r",
           "r":"t", "s":"y",
           "t":"p", "v":"t",
           "w":"j", "x":"k",
           "z":"b"}


def täht(sisend:list):
    for taht in sisend:
        print(str(tahestik.index(taht))+" ", end="")

def keemia(sisend:list):
    lopp = ""
    for täht in sisend:
        if täht in keemias.keys():
            lopp += (str(keemias.get(täht))) + " "
        else:
            lopp += "0 "
    print(lopp)

def caesar(sisend:list, mitu:int):
    lopp = ""
    for täht in sisend:
        if täht in tahestik[1:]:
            asd = tahestik.index(täht)
            lopp += (tahestik[asd + mitu - len(tahestik)])
        else:
            lopp += täht
    print(lopp)

def telefon(sisend:list):
    lopp = ""
    for täht in sisend:
        try:
            for number in range(len(telo)):
                if täht in telo[number]:
                    lopp += (str(number + 1) * (telo[number].index(täht) + 1))
        except: pass
    print(lopp)

def atbash(sisend:list):
    lopp = ""
    for täht in sisend:
        if täht in tahestik.strip():
            lopp += (tahestik.strip()[-(tahestik.index(täht)) - 1])
        else:
            lopp += (täht)
    print("".join(lopp))

def vigenere(sisend:list, kood:list):
    lopp = ""
    asd = tahestik[1:]
    for täht in range(len(sisend)):
        lopp += asd[asd.index(sisend[täht])+asd.index(kood[täht % len(kood)])-len(asd)]
    print(lopp)

def binary(sisend:list):
    lõpp = ""
    for arv in sisend:
        if arv.isnumeric():
            arv = int(arv)
            lopp = []
            for aste in range(32):
                if arv // 2 ** (31 - aste) >= 1:
                    lopp.append("1")
                    arv -= 2 ** (31 - aste)
                else:
                    lopp.append("0")

        while lopp[0] == "0":
            lopp.pop(0)
        lõpp += "".join(lopp) + " "
    print(lõpp)

def morse(sisend:list):
    lopp = ""
    for täht in sisend:
        try:
            lopp += morse.get(täht) + " "
        except:
            pass
    print(lopp)

def corpus(sisend:list):
    lopp = ""
    for täht in sisend:
        if täht in corpusL.keys():
            if täht.isupper():
                lopp += corpusL.get(täht.lower()).upper()
            else:
                lopp += corpusL.get(täht)
        else:
            lopp += täht
    print(lopp)

while True:
    yeet = input("Mis kodeering(keemia, täht, caesar, telefon, atbash, kinni, vigenere, binary, morse, corpus)").lower()

    if yeet == "kinni":
        print("Bye")
        break

    if yeet == "täht":
        sisend = list(input("Anna sõne: ").lower())
        täht(sisend)

    elif yeet == "keemia":
        sisend = list(input("Anna sõne: ").lower())
        keemia(sisend)

    elif yeet == "caesar":
        sisend = list(input("Anna sõne: ").lower())
        mitu = int(input("Mitu kohta: "))
        caesar(sisend, mitu)


    elif yeet == "telefon":
        sisend = list(input("Anna sõne: ").lower())
        telefon(sisend)

    elif yeet == "atbash":
        sisend = list(input("Anna sõne: ").lower())
        atbash(sisend)


    elif yeet == "vigenere":
        sisend = list("".join(input("Sõne: ").lower().strip(" ").split(" ")))  # teeb tähed väikeseks, eemaldab tühikud, teeb listi stringiks ja uuesti listiks
        kood = list(input("Kood(üks sõna): ").lower())
        vigenere(sisend, kood)


    elif yeet == "binary":
        sisend = list(input("Anna arv(ud): ").split(" "))
        binary(sisend)


    elif yeet == "morse":
        sisend = list(input("Anna sõne: "))
        morse(sisend)

    elif yeet == "corpus":
        sisend = list(input("Anna sõne: "))
        corpus(sisend)

    #lõpu tühik
    print("\n")