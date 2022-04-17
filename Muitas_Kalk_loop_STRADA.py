from math import*
from sys import*

kopm = 0
kops = 0

def atkārtot():
    min=int(input("Vai pasūtījuma summa pārsneidz 150 eiro? Jā - 1 Nē - 2\n - "))
    if min == 1:
        print("Tālāk:")
    elif min == 2:
        print("Muita nav jāmaksā")
        input("Pispiediet Enter lai beigtu programmu")
        exit()
    else:
        print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
        atkārtot()

def valsts():
    ES = int(input("Vai piegādātājs ir ārpus Eiropas Savienības? Jā - 1 Nē - 2\n - "))
    if ES == 1:
        print("Tālāk:")
    elif ES == 2:
        print("Muita nav jāmaksā")
        input("Piespiediet Enter lai beigtu programmu")
        exit()
    else:
        print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
        valsts()




atkārtot()
valsts()
reiz=float(input("Cik kopeji preces ir pirkumā?\n - "))

for i in (1,reiz):
    naud = float(input("Cik liela ir preces summa?\n - "))
    kas=int(input("Vai prece ir taborēta vai adīta? Jā - 1 Nē - 2\n - " ))
    if kas == 1:
        AT=int(input('''Lūdzu izvēlaties kurā no kategorijām ietilps jūsu prece:\n
        1)Svīteri un puloveri, ar vilnas saturu vismaz 50 % - 1\n  
        2)Mazu bērnu cimdi; Peldapģerbs kurā 5% no masas vai vairāk;Graudētas kopresijas zeķes no sintētiskajām šķiedrām;\n
        Trikotāžas cimdipirkstaiņi, impregnēti, apvalkoti vai pārklāti ar gumiju - 2\n
        3)Trikotāžas cimdi citādi - 3\n
        4)Neviens no iepriekš minētajiem - 4\n'''))
        if AT == 1:
            plus = naud*10.5/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa," EUR, muitas daudzums ir" ,plus," EUR")
        elif AT == 2:
            plus = naud*8/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)         
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa, " EUR, muitas daudzums ir" ,plus," EUR")
        elif AT == 3:
            plus = naud*8.9/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)         
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa," EUR, muitas daudzums ir" ,plus," EUR")
        elif AT == 4:
            plus = naud*12/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)         
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa," EUR, muitas daudzums ir" ,plus," EUR")
        else:
            print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
            prece(naud)
    elif kas == 2:
        print("Prece nav adīta vai tamborēta.")
        NAT=int(input('''Lūdzu izvēlaties kurā no kategorijām ietilps jūsu prece:\n
         1)Mazu bērnu apģērbi un apģērba piederumi - 1\n  
         2)Krūšturi, zeķturi, korsetes, bikšturi, prievītes un tamlīdzīgi izstrādājumi un to daļas, arī no trikotāžas - 2\n
         3)Kabatlakati - 3\n
         4)Šalles, lakati, kaklauti, mantiļas, plīvuri un tamlīdzīgi izstrādājumi - 4\n
         5)Kaklasaites, tauriņi un kravates - 5\n
         6)Cimdi(pirkstaiņi dūraiņi) - 6\n
         7)Neviens no iepriekš minētajiem - 7\n'''))
        if NAT == 1:
            plus = naud*10.5/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa," EUR, muitas daudzums ir" ,plus," EUR")
        elif NAT == 2:
            plus = naud*6.5/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)    
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa, " EUR, muitas daudzums ir" ,plus," EUR")
        elif NAT == 3:
            plus = naud*10/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)       
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa," EUR, muitas daudzums ir" ,plus," EUR")
        elif NAT == 4:
            plus = naud*8/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)  
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa," EUR, muitas daudzums ir" ,plus," EUR")
        elif NAT == 5:
            plus = naud*6.3/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)       
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa," EUR, muitas daudzums ir" ,plus," EUR")
        elif NAT == 6:
            plus = naud*7.6/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)      
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa," EUR, muitas daudzums ir" ,plus," EUR")
        elif NAT == 7:
            plus = naud*12/100
            summa = naud+plus
            plus = round(plus,2)
            summa = round(summa,2)      
            print("Summa kas jāapmaksā kopā ar muitu ir" ,summa," EUR, muitas daudzums ir" ,plus," EUR")
        else:
            print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
            prece(naud)
    else:
        print ("Lūdzu izvēlaties vienu no piedāvātajā atbilžu opcijām.")
        prece(naud)
    kopm += plus
    kops += summa

    
    
print("Kopējā summa ar muitu ir" ,kops, "EUR" )
print("Muitas daudzums ir" ,kopm, "EUR ")
input("Pispiediet Enter lai beigtu programmu")