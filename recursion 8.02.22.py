import turtle as t
import os.path

def ul1(aste, pikkus):
    if aste == 0:
        pass
    elif aste%2 == 1:
        for i in range(3):
            t.forward(pikkus)
            ul1(aste-1, pikkus / 3)
            t.left(60)
            t.forward(pikkus)
            t.left(60)

    elif aste%2 == 0:
        for i in range(3):
            t.forward(pikkus)
            ul1(aste-1, pikkus / 3)
            t.right(60)
            t.forward(pikkus)
            t.right(60)

def ul2(otsitav, koht, kogus):
    if koht == [] or kogus < 0:
        return (kogus == 0)
    else:
        if koht[0] == otsitav:
            return ul2(otsitav, koht[1::], kogus-1)
        else:
            return ul2(otsitav, koht[1::], kogus)


def ul3(files, aste):
    if aste == 0:
        print(files)
        ul3(files, aste+1)
    if not os.path.isdir(files):
        return "ÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄÄ"
    else:
        for i in os.listdir(files):
            taisnimi = os.path.join(files, i)
            if os.path.isdir(taisnimi):
                print(aste*"   "+os.path.basename(i))
                ul3(taisnimi, aste+1)
            else:
                print(aste * "   " + os.path.basename(i))

def ul4(aste, suurus):
    if aste == 0:
        for i in range(4):
            t.forward(suurus)
            t.right(90)
    else:
        for i in range(2):
            ul4(aste-1, (suurus-1)/2)
            t.forward(suurus)
            t.right(90)
            t.forward(suurus)
            t.right(90)

def ul5(aste, suurus):
    if aste >= 0:
        for i in range(2):
            for i in range(2**aste):
                t.forward(suurus / (2**aste))
                t.right(90)
                t.forward(suurus / (2**aste))
                t.left(90)
            t.left(180)
        ul5(aste-1, suurus)


if __name__ == "__main__":
    t.speed(-1)
    t.delay(0)
    #ul1(3, 100)
    #print(ul2("a",["a","b","a"],2))
    #ul3("C:\\DRIVERS", 0)
    #ul4(2,100)
    t.pu()
    t.goto(-300, 300)
    t.pd()
    ul5(3,600)


    t.exitonclick()