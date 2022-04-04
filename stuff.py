import os
import base64
from time import sleep
import random

Users = "TWFydF9LYWFyZW1hYSBKb2hhbm5lc19UYW1tIENhcmxvc19MZXBhbWFhIEtlcnQtS2FsdmluX0dyZW50c21hbm4gVmFsZG9fU29sw6R0dGUgVGFuZWxfTWlya2EgVMO1bnVfS3V0c2FyIEFybm9sZF9Mb29nYQ=="
Locate = "TGFwaW1hYSBUYWxsaW5uIFg6NjQ2Mjc3NV9ZOjY0ODU3NCBUYXJ0dSBUYWxsaW5uIFZhbGdhIFN0b2NraG9sbSBVbmtub3du"
Ids = "MTAwOTEyMjQgMTAwMDkzMjQyIDEwMDA5NzQ1MyAxMDAwOTEwMDIgMTAwMDk3NDMyIDEwMDA5MjMzMiAxMDAwOTczMjQgMTAwMDg5Mzc0"

def Caesar(string, aste):
    tahed = "abcdefghijklmnopqrsšzžtuvwõäöüxy"
    lopp = ""
    for i in string:
        if i.isupper():
            lopp += tahed[(tahed.index(i.lower())+aste)%len(tahed)].upper()
        else:
            lopp += tahed[(tahed.index(i) + aste) % len(tahed)]
    return lopp

while True:
    sisend = input("ID: ")
    if sisend in base64.b64decode(Ids.encode("UTF-8")).decode("UTF-8").split(" "):
        sisend = input("Password: ")
        print(base64.b64decode("a2Fsa3VuaXByYWVsYXVka29sbXR1aGF0".encode("UTF-8")).decode("UTF-8"))
        if sisend == base64.b64decode("a2Fsa3VuaXByYWVsYXVka29sbXR1aGF0".encode("UTF-8")).decode("UTF-8"):
            break
        else:
            os.system('cls')
            print("Wrong password")
    else:
        os.system('cls')

os.system('ping 195.50.209.246')

while True:
    os.system("cls")
    print("Connected: Anonymous data distribution server - Estonia")
    print("Connection: secure")
    print("We are legion. We do not forget. We do not forgive. Expect us.")
    print("""
                            ░░░░░░░░░░░░░░░░░░░░░░                    
                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░              
                ░░░░░░░░      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒        
            ░░░░░░░░                  ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒    
          ░░░░░░░░░░                    ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒  
        ░░░░░░░░░░░░░░                  ░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒  
        ░░░░░░░░░░░░░░░░░░              ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒
        ░░░░░░  ░░        ░░            ░░  ░░░░░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒
      ░░░░░░░░▓▓██▓▓▒▒░░░░  ░░              ░░▒▒▓▓▓▓██▓▓▓▓▓▓██▓▓▒▒▒▒▒▒
        ░░▒▒░░░░░░░░▒▒▒▒░░░░░░          ░░████████░░░░░░░░░░░░░░▒▒▒▒▒▒
      ░░░░░░░░        ░░▒▒▓▓▓▓          ▓▓██▒▒░░  ░░░░░░░░░░░░░░▒▒▒▒▒▒
      ▒▒░░░░            ░░░░▓▓          ▓▓░░░░    ░░░░  ░░░░░░░░▒▒▒▒▒▒
      ▒▒░░░░              ░░░░          ░░░░      ░░░░░░░░░░░░░░▒▒▒▒▒▒
      ▒▒░░░░░░            ░░░░        ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒
      ░░░░░░░░░░    ░░░░░░░░          ░░░░░░░░░░▓▓██████▓▓░░░░▒▒▒▒▒▒▒▒
      ░░░░░░░░▒▒██████████░░          ░░░░░░████████████████░░▒▒▒▒▒▒▒▒
      ░░░░░░░░██████████▓▓▓▓          ░░░░░░██████████████▓▓░░░░░░▒▒▒▒
      ░░░░░░░░░░▓▓██▓▓▒▒░░            ░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒
      ░░░░░░░░░░░░░░░░                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒
      ░░░░░░░░░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒
      ░░░░░░░░░░░░                  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒
      ░░░░░░░░░░                    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓
      ░░░░░░░░░░                      ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓
      ░░░░░░░░░░░░                    ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒
      ░░░░░░░░░░░░  ░░░░░░            ░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒  
        ░░░░░░░░░░░░                  ░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒  
        ▒▒  ▒▒▒▒░░        ░░          ░░░░░░░░░░░░░░░░░░░░░░██░░▒▒▒▒  
        ▒▒░░░░██░░          ░░░░░░  ░░░░▒▒░░░░░░░░░░░░░░░░▓▓▓▓░░▒▒▒▒  
        ░░░░░░▓▓▒▒            ░░██▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░▒▒██▒▒░░▒▒    
        ░░░░  ░░██▒▒      ░░▒▒▓▓▓▓▒▒░░▓▓▓▓▓▓░░░░░░░░░░▓▓██▒▒▒▒▒▒▒▒    
          ░░░░  ░░▓▓▓▓▓▓▒▒▓▓▓▓▒▒▓▓░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░▒▒░░▒▒▒▒    
          ░░░░  ░░░░▓▓▓▓▓▓▓▓▓▓▓▓░░    ░░██▒▒▓▓▓▓▓▓▒▒░░░░▒▒░░▒▒▒▒      
          ░░░░░░  ░░    ░░░░██▒▒▒▒▒▒▒▒▓▓▓▓▓▓░░░░░░░░░░▒▒░░░░▒▒▒▒      
            ░░░░░░  ░░░░              ░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒▒▒        
              ░░░░░░░░░░░░░░░░          ░░░░░░▒▒░░▒▒▒▒░░▒▒▒▒          
                  ░░░░░░░░░░    ▒▒▓▓▓▓██▒▒░░░░░░░░▒▒░░▒▒▒▒            
                  ░░░░░░░░░░░░░░  ██████░░░░░░░░▒▒░░▒▒▒▒              
                    ░░░░░░░░      ▓▓██▓▓░░░░░░░░▒▒▒▒▒▒▒▒              
                      ░░░░░░░░  ░░▓▓████░░░░░░░░▒▒▒▒▒▒                
                        ░░░░░░░░░░▓▓██▓▓░░░░░░▒▒▒▒░░                  
                          ░░░░░░░░██████░░░░░░▒▒                      
                            ░░░░░░▓▓████▒▒░░▒▒                        
                              ░░░░▒▒████▒▒▒▒                          
                                  ░░██▓▓░░  
                                                            
    """)
    sisend = input("Action(Users/Recent/History/Exit): ").lower()
    if sisend == "recent":
        print("No activity found in 7 days")
        sleep(2)
    elif sisend == "history":
        print("Last Login: 22/06/2018")
        print("Login location: *Missing*")
        sleep(2)
    elif sisend == "users":
        os.system('cls')
        for key in range(len(base64.b64decode(Users.encode("UTF-8")).decode("UTF-8").split(" "))):
            sleep(3**random.random()/5)
            print("User: "+base64.b64decode(Users.encode("UTF-8")).decode("UTF-8").split(" ")[key])
            print("ID: "+base64.b64decode(Ids.encode("UTF-8")).decode("UTF-8").split(" ")[key])
            print("Last location: "+base64.b64decode(Locate.encode("UTF-8")).decode("UTF-8").split(" ")[key])
            print("")
        input("Press enter to go back")
    elif sisend == "exit":
        os.system('cls')
        print("Connection terminated...")
        sleep(2)
        break
