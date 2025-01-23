import tad_poli as tP
def main():
    polinomio1 = tP.new_poli('3x2+2x+1')
    polinomio2 = tP.new_poli('2x2+3x+1')
    soma = tP.soma_poli(polinomio1, polinomio2)
    subtração = tP.subtrai_poli(polinomio1, polinomio2)
    multiplicação = tP.multiplica_poli(polinomio1, polinomio2)
    print(f"Polinomios formados:\n{polinomio1}\n{polinomio2}")
    print(f"\nOperações:\n{'Soma':<24}{'Subtração':<25}{'Multiplicação':>10}")
    print(f"{soma}      {subtração}      {multiplicação}")
main()