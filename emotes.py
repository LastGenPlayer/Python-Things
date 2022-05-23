"""
from tkinter import *

raam = Tk()
raam.title("Emotikon")
w = 500
h = 500
tahvel = Canvas(raam, width=w, height=h, background="white")
tahvel.grid()

tahvel.create_oval(50, 50, 450, 450, width= 17, fill="yellow")
tahvel.create_oval(180,280, 320,420, fill="black")
tahvel.create_oval(120,160, 200,240, fill="black")
tahvel.create_oval(300,160, 380,240, fill="black")

raam.mainloop()"""
file = open("juut.txt", "w", encoding="utf-8")
count = 0
for n in range(1,6):
    for l in range(n):
        for m in range(l+1):
            print("n: "+str(n)+" l: "+str(l)+" mL: "+str(m)+" s: 0.5")
            print("n: " + str(n) + " l: " + str(l) + " mL: " + str(m) + " s: -0.5")
            #file.write("n:"+str(n)+" l:"+str(l)+" mL:"+str(m)+" s:0.5\n")
            file.write("n:" + str(n) + " l:" + str(l) + " mL:" + str(m) + " s:±0.5\n\n")
            print()
            count += 2
            if m!=0:
                print("n:" + str(n) + " l: " + str(l) + " mL: -" + str(m) + " s: 0.5")
                print("n:" + str(n) + " l: " + str(l) + " mL: -" + str(m) + " s: -0.5")
                #file.write("n:" + str(n) + " l:" + str(l) + " mL:-" + str(m) + " s:0.5\n")
                file.write("n:" + str(n) + " l:" + str(l) + " mL:-" + str(m) + " s:±0.5\n\n")
                print()
                count += 2
print(count)