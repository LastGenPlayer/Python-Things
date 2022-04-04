täpid = {27:"Õ",28:"Ä",29:"Ö",30:"Ü"}
keemia ={"a":18,"b":5,"c":6,"d":66,"e":63,"f":9,"g":31,"h":1,"i":53,"j":53,"k":19,"l":3,"m":12,"n":7,"o":8,"p":15,"q":"6*","r":44,"s":16,"t":22,"u":92,"v":74,"w":74,"x":54,"y":23,"z":40}
telo = ["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

while True:
    yeet = input("Mis cipher on(täht, telefon, atbash, binary):")
    if yeet == "binary":
        sisend = input("Kood: ").split(" ")
        lõpp = []
        for arv in sisend:
            lopp = 0
            if arv.isnumeric():
                for i in range(32):
                    try:
                        lopp += int(arv[-i-1])*2**i
                    except:
                        asd = 0

                lõpp.append(str(lopp))
        print(" ".join(lõpp))


    elif yeet == "täht":
        sisend = input("numbrid: ").split(" ")
        lopp = ""
        for number in sisend:
            if number == "0":
                lopp += " "
            elif int(number) in täpid:
                lopp += täpid.get(int(number))
            else:
                lopp += chr(int(number)+64)
        print(lopp.lower())

    elif yeet == "atbash":
        sisend = input("sõne: ").lower()
        lopp = []
        for täht in sisend:
            lopp.append(atbash[-(atbash.index(täht))-1])
        print("".join(lopp))

    elif yeet == "telefon":
        sisend = list(input("Anna number").strip().split(" "))
        mitu = 0
        mis = sisend[0]
        lopp = ""
        sisend.append("#")
        while " " in sisend:
            sisend.remove(" ")
        for täht in sisend:
            try:
                if "0"in täht:
                    lopp += " "
                else:
                    lopp+=(telo[int(täht[0])-2][len(täht)-1])
            except:
                print(lopp)