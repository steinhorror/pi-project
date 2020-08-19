from decimal import Decimal, getcontext


def getPi(nks=100):
    getcontext().prec=nks
    res = sum(1/Decimal(16)**k * 
              (Decimal(4)/(8*k+1) - 
               Decimal(2)/(8*k+4) - 
               Decimal(1)/(8*k+5) -
               Decimal(1)/(8*k+6)) for k in range(100))
    return res
