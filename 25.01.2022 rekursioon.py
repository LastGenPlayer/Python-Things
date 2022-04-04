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

def kuulujutud2(rahvas, aste):
    if rahvas <= 1:
        return aste
    else:
        return kuulujutud2(rahvas/4, aste+1)

def vokaalid(rida):
    vokaal = "aeiouõäöü"
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

#ignore this
def backwards(word):
    return word[::-1]

def euler15(x, y):
    if x == 1:
        return 1
    elif y == 1:
        return 1
    else:
        return euler15(x-1,y) + euler15(x,y-1)


if __name__ == "__main__":
    #print(otsi("K:\\tested\\Muusika"))
    #arvamismäng(5, 12)
    print(kuulujutud2(16, 0))
    print(vokaalid("kapitalist"))
    print(tagurpidi("aasd"))