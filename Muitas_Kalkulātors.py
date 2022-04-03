from math import*
from sys import*

def atkārtot1():
    min=int(input("Vai pasūtījuma summa pārsneidz 150 eiro? Jā - 1 Nē - 2  "))
    if min == 1:
        print("Tālāk:")
    elif min == 2:
        print("muita nav jāmaksā")
        exit()
    else:
        print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
        atkārtot1()

def atkārtot2():
    kas=int(input("Vai prece ir taborēta vai adīta? Jā - 1 Nē - 2  " ))
    if kas == 1:
        print("Adīts_Tamborēts")
    elif kas == 2:
        print("Pārējais")
    else:
        print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
        atkārtot2()
atkārtot1()
atkārtot2()