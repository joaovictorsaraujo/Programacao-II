def new_eq(ca, cb, cc):
    equacao = {'A':int(ca), 'B':int(cb), 'C':int(cc)}
    return equacao

def getA(tad):
    return tad['A']

def getB(tad):
    return tad['B']

def getC(tad):
    return tad['C']

def _delta(eq):
    return (eq['B']**2) - (4 * eq['A'] * eq['C'])

def quant_raizes(tad):
    delta = _delta(tad)
    if delta < 0:
        return 0
    elif delta == 0:
        return 1
    else:
        return 2

def getRaiz1(tad):
    delta = _delta(tad)
    if quant_raizes(tad) >= 1:
        raiz1 = (((- tad['B']) + ((delta)**(1/2))) / (2 * tad['A']))
        return raiz1
    else:
        return 'Nenhuma raíz real'
    
def getRaiz2(tad):
    delta = _delta(tad)
    if quant_raizes(tad) == 2:
        raiz2 = (((- tad['B']) - ((delta)**(1/2))) / (2 * tad['A']))
        return raiz2
    elif quant_raizes(tad) == 1:
        return 'Há somente uma raíz'
    else:
        return 'Nenhuma raíz real'