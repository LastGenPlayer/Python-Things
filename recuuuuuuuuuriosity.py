
def ul9(file):
    file = open(file,"r")
    yeets = {}

    for line in file:
        line = line.strip().split(":")
        nimi = line[0]
        vanemad = line[1].replace(",","").strip().split(" ")
        yeets[nimi] = vanemad
    return yeets


def on_eellane(nimi, vanem):
    if nimi in heterod.keys():
        vanemad = heterod.get(nimi)
        if vanemad[0] == vanem or vanemad[1] == vanem:
            return True
        else:
            return on_eellane(vanemad[0], vanem) or on_eellane(vanemad[1], vanem)
    else:
        return False

def rek_abs(last):

    if isinstance(last, list):
        last = rek_abs(last)
    else:
        last = abs(last)



if __name__ == "__main__":
    heterod = ul9("sugupuu.txt")
    print(on_eellane("Kalle", "Siim"))
    print(on_eellane("Rita","Joosep"))
    print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))