import turtle as t

def spiraal(size, muut):
    if size > 0:
        t.forward(size)
        t.right(90)
        spiraal(size - muut, muut)


def ümarspiraal(size, muut):
    if size > 0:
        t.circle(size, 90)
        ümarspiraal(size-muut, muut)

def fraktal1(size, aste):
    if aste >= 1:
        t.forward(size)
        t.left(90)
        fraktal1(size*0.72, aste-1)
        t.left(180)
        fraktal1(size*0.72, aste - 1)
        t.left(90)
        t.back(size)

def pikkus(list):
    if list != []:
        return pikkus(list[1::]) + 1
    else:
        return 0

def kuulujutud(aste):
    if aste == 0:
        return 1
    return kuulujutud(aste-1)+kuulujutud(aste-1)+kuulujutud(aste-1)+kuulujutud(aste-1)

def küülikud(noored: int, vanad: int, kuu: int):
    if kuu == 0:
        return int(noored+vanad)
    return küülikud(vanad, noored+vanad, kuu-1)

def paremküülik(aeg_kuudes):
    if aeg_kuudes <= 1:
        return 1
    else:
        return paremküülik(aeg_kuudes-2)+paremküülik(aeg_kuudes-1)

def fraktal3(aste, suurus):
    t.speed(-1)
    t.delay(0)
    if aste != 0:
        fraktal3(aste - 1, suurus)
        t.left(60)
        fraktal3(aste - 1, suurus)
        t.right(120)
        fraktal3(aste - 1, suurus)
        t.left(60)
        fraktal3(aste - 1, suurus)
    else:
        t.forward(suurus)

if __name__ == "__main__":
    for i in range(3):
        fraktal3(3, 30)
        t.right(120)

    #print(kuulujutud(10))
    #print(küülikud(1,0,50))
    #print(pikkus([1,2,3,4,5,6,7,8]))
    #print(paremküülik(50))

    t.exitonclick()
