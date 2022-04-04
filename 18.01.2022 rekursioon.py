import os.path

def otsi(path):
    if not os.path.isdir(path):
        return os.path.basename(path)

    else:
        kaust = []
        for i in os.listdir(path):
            täisnimi = os.path.join(path, i)
            kaust.append(otsi(täisnimi))

        return kaust

def arvamismäng(pakkumised, arv):
    if pakkumised != 0:
        sisend = int(input("Paku arvu (katseid: "+ str(pakkumised) +"): "))

        if sisend == arv:
            print("Õige arv :)")
            return True

        elif sisend > arv:
            print("Paku väiksemalt")
            arvamismäng(pakkumised-1, arv)

        elif sisend < arv:
            print("Paku suuremalt")
            arvamismäng(pakkumised-1, arv)

    else:
        print("Ei teinud ära :(")

def kuulujutud2(rahvas, aste, palju):
    if rahvas >= palju:
        return aste
    else:
        return kuulujutud2(rahvas*4, aste+1, palju)

def vokaalid(rida):
    vokaal = ["a","e","i","o","u","õ","ä","ö","ü"]
    if len(rida) == 0:
        return ""
    else:
        if rida[0].lower() in vokaal:
            return vokaalid(rida[1:])
        else:
            return rida[0] + vokaalid(rida[1:])

def tagurpidi(sone):
    if len(sone) == 0:
        return ""
    else:
        return tagurpidi(sone[1:]) + sone[0]


if __name__ == "__main__":
    print(otsi("C:\\DRIVERS"))
    #arvamismäng(5, 12)
    #print(kuulujutud2(1, 0, 16))
    print(vokaalid("kapitalist"))
    print(tagurpidi("aasd"))