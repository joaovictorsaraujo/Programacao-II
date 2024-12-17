import tadequacao as te
import os
def main():
    equacao = te.new_eq(input(), input(), input())
    os.system('cls')
    print(te.getA(equacao), te.getB(equacao), te.getC(equacao), te.quant_raizes(equacao), te.getRaiz1(equacao), te.getRaiz2(equacao))
main()
