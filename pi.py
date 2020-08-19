from decimal import Decimal, getcontext


def getPi(nks=100):
    getcontext().prec=nks
    res = sum(1/Decimal(16)**k * 
              (Decimal(4)/(8*k+1) - 
               Decimal(2)/(8*k+4) - 
               Decimal(1)/(8*k+5) -
               Decimal(1)/(8*k+6)) for k in range(100))
    return res
print("In wie vielen Nachkommastellen willst du suchen?")
inpu = int(input())
sm = getPi(inpu)
print("Zahl bitte:")
search = input()
print("Pi =  " + str(sm))
sm = str(sm).split(".")[1]
sm = sm.find(search)
if(sm == -1) :
    print("Diese Zahl existiert nicht in den ersten " + str(inpu) + " Nachkommastellen")
print("Die zu suchende Zahl befindet sich an der " + str(sm) + ". Nachkommastelle")
