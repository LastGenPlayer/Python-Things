"""
from random import random

for  i in range(20):
    kuu = int(random()*12)+1
    päev =int(random()*28)+1

    if kuu < 10:
        kuu = "0"+str(kuu)
    if päev < 10:
        päev = "0"+str(päev)

    print(f"2021-{kuu}-{päev}")
"""

from tkinter import *
from math import sin

raam = Tk()
raam.title("Lill")
w = 500
h = 500
tahvel = Canvas(raam, width=w, height=h, background="white")
tahvel.grid()

punktid1 = [250,250, 260,400, 285,370, 310,390, 320,360, 360,375]
punktid2 = []
punktid3 = []
punktid4 = []
punktid5 = []
punktid6 = []
punktid7 = []
punktid8 = []


for i in range(int(len(punktid1)/2)):
    punktid2.append(punktid1[2*i + 1])
    punktid2.append(punktid1[2*i])

for i in range(int(len(punktid1)/2)):
    punktid3.append(500-punktid1[2*i])
    punktid3.append(punktid1[2*i + 1])
    punktid4.append(500 - punktid2[2 * i])
    punktid4.append(punktid2[2 * i + 1])

    punktid5.append(punktid1[2 * i])
    punktid5.append(500-punktid1[2 * i + 1])
    punktid6.append(punktid2[2 * i])
    punktid6.append(500-punktid2[2 * i + 1])

    punktid7.append(500 - punktid1[2 * i])
    punktid7.append(500 - punktid1[2 * i + 1])
    punktid8.append(500 - punktid2[2 * i])
    punktid8.append(500 - punktid2[2 * i + 1])


tahvel.create_polygon(punktid1, fill="blue")
tahvel.create_polygon(punktid2, fill="blue")
tahvel.create_polygon(punktid3, fill="blue")
tahvel.create_polygon(punktid4, fill="blue")
tahvel.create_polygon(punktid5, fill="blue")
tahvel.create_polygon(punktid6, fill="blue")
tahvel.create_polygon(punktid7, fill="blue")
tahvel.create_polygon(punktid8, fill="blue")


#c00101 punane
#00ebfd sinine
#000000 must

raam.mainloop()