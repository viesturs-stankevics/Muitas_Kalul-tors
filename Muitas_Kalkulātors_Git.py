from math import*
from sys import*

def atkārtot():
    min=int(input("Vai pasūtījuma summa pārsneidz 150 eiro? Jā - 1 Nē - 2  "))
    if min == 1:
        print("Tālāk:")
    elif min == 2:
        print("muita nav jāmaksā")
        exit()
    else:
        print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
        atkārtot()

def valsts():
    ES = int(input("Vai piegādātājs ir ārpus Eiropas Savienības? Jā - 1 Nē - 2  "))
    if ES == 1:
        print("Tālāk:")
    elif ES == 2:
        print("muita nav jāmaksā")
        exit()
    else:
        print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
        valsts()

def prece():
    kas=int(input("Vai prece ir taborēta vai adīta? Jā - 1 Nē - 2  " ))
    if kas == 1:
        print("Prece ir adīta vai tamborēta.")
    elif kas == 2:
        print("Prece nav adīta vai tamborēta.")
    else:
        print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
        prece()

atkārtot()
valsts()
prece()
