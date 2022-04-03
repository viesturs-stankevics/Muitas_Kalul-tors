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

atkārtot()