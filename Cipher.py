täpid = {"Õ":27,"Ä":28,"Ö":29,"Ü":30}
keemia ={"a":18,"b":5,"c":6,"d":66,"e":63,"f":9,"g":31,"h":1,"i":53,"j":53,"k":19,"l":3,"m":12,"n":7,"o":8,"p":15,"q":"6*","r":44,"s":16,"t":22,"u":92,"v":74,"w":74,"x":54,"y":23,"z":40}
telo = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
atbash = " abcdefghijklmnopqrsšzžtuvwõäöüxy"
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

corpusL = {"b":"t",
           "c":"y",
           "d":"p",
           "f":"t",
           "g":"j",
           "h":"k",
           "j":"t",
           "l":"p",
           "m":"s",
           "n":"t",
           "p":"k",
           "q":"r",
           "r":"t",
           "s":"y",
           "t":"p",
           "v":"t",
           "w":"j",
           "x":"k",
           "z":"b"}

while True:
    yeet = input("Mis kodeering(keemia, täht, caesar, telefon, atbash, kinni, vigenere, binary, morse, corpus):").lower()

    if yeet == "täht":
        sisend = input("sõne: ").lower()
        lopp = []
        for täht in sisend:
            lopp.append(str(atbash.index(täht)))
        print(" ".join(lopp)+"\n")


    elif yeet == "keemia":
        sisend = input("sõne: ").lower()
        lopp = []
        for täht in sisend:
            try:
                if täht != " ":
                    lopp.append(str(keemia.get(täht)))
                else: lopp.append("0")
            except:
                lopp.append(täht)
        print(" ".join(lopp))

    elif yeet == "caesar":
        sisend = input("sõne: ").lower()
        mitu = int(input("Mitu kohta: "))
        lopp=[]
        for täht in sisend:
            if täht in atbash:
                asd = atbash.index(täht)
                lopp.append(atbash[asd+mitu-30])
            else:
                lopp.append(täht)
        print("".join(lopp))


    elif yeet == "telefon":
        sisend = input("sõne: ")
        lopp=[]
        for täht in sisend:
            if täht == " ":
                lopp.append("0")
            else:
                for number in range(len(telo)):
                    if täht in telo[number]:
                        lopp.append(str(number+2)*(telo[number].index(täht)+1))
        print(" ".join(lopp))


    elif yeet == "kinni":
        print("Bye")
        break


    elif yeet == "atbash":
        sisend = input("sõne: ").lower()
        lopp = []
        for täht in sisend:
            if täht in atbash.strip():
                lopp.append(atbash.strip()[-(atbash.index(täht))-1])
            else:
                lopp.append(täht)
        print("".join(lopp))


    elif yeet == "vigenere":
        sisend = input("Sõne: ").upper().strip(" ").split(" ")
        kood = input("Kood: ").upper()
        sisend = "".join(sisend)
        lopp = []
        asd =[]
        for täht in kood:
            if täht == "Õ" or täht == "Ä" or täht == "Ö" or täht == "Ü":
                asd.append(täpid.get(täht))
            else:
                asd.append(ord(täht)-64)
        asd = asd*round((len(sisend)/len(kood))+1)
        for täht in range(len(sisend)):
            if sisend[täht] == "Õ" or sisend[täht] == "Ä" or sisend[täht] == "Ö" or sisend[täht] == "Ü":
                lopp.append(chr((täpid.get(sisend[täht])+asd[täht]-1)-(täpid.get(sisend[täht])+asd[täht]-1)//65))
            else:
                lopp.append(chr(ord(sisend[täht])-65+(asd[täht]-1)-(ord(sisend[täht])-65+(asd[täht]-1))//26*26+65))
        print(" ".join(lopp))


    elif yeet == "binary":
        sisend = input("Anna number: ").split(" ")
        lõpp = []
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

                null = 0
                for number in range(32):
                    if lopp[number] == "0":
                        null += 1
                    elif lopp[number] == "1":
                        break
                for yes in range(null):
                    if len(lopp) > 1:
                        lopp.remove("0")
            lõpp.append("".join(lopp))
            lõpp.append(" ")
        print("".join(lõpp))


    elif yeet == "morse":
        lopp = ""
        sisend = list(input("anna sõne: "))
        for täht in sisend:
            try:
                lopp += morse.get(täht)+" "
            except:
                pass
        print(lopp)


    elif yeet == "corpus":
        lopp = ""
        sisend = list(input("Anna sõne: "))
        for täht in sisend:
            if täht in corpusL.keys():
                if täht.isupper():
                    lopp += corpusL.get(täht.lower()).upper()
                else:
                    lopp += corpusL.get(täht)
            else:
                lopp += täht
        print(lopp)

    #lõpu tühik
    print("\n")

