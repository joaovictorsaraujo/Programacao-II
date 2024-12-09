def sem_acento(texto):

    t = ''

    for i in texto:
        if(i in 'áàãâ'):
            t += 'a'
        elif(i in 'éèê'):
            t += 'e'
        elif(i in 'íìî'):
            t += 'i'
        elif(i in 'óòõô'):
            t += 'o'
        elif(i in 'úùû'):
            t += 'u'
        elif(i in 'ÁÀÃÂ'):
            t += 'A'
        elif(i in 'ÉÈÊ'):
            t += 'E'
        elif(i in 'ÍÌÎ'):
            t += 'I'
        elif(i in 'ÓÒÕÔ'):
            t += 'O'
        elif(i in 'ÚÙÛ'):
            t += 'U'
        else:
            t += i
    return t    

def main():

    texto = input()
    print(sem_acento(texto))

if __name__ == "__main__":
    main()
    