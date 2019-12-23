def calculateFine(diaDevuelto,fechaEsperadaDeDevolucion):
    if diaDevuelto[2] == fechaEsperadaDeDevolucion[2]: # mismo año
        if diaDevuelto[1] <=fechaEsperadaDeDevolucion[1]: # mismo mes o menor
            if diaDevuelto[0] < fechaEsperadaDeDevolucion[0]:
                return 0
            else:
                return 15 * (diaDevuelto[0] - fechaEsperadaDeDevolucion[0])
        else:
            return 500 * (diaDevuelto[1]-fechaEsperadaDeDevolucion[1]) #mes mayor
    else:
        if diaDevuelto[2] > fechaEsperadaDeDevolucion[2]:
            return 10000
        else:
            return 0





if __name__ == '__main__':

    diaDevuelto=input().split(' ')
    fechaEsperadaDeDevolucion =input().split(' ')
    diaDevuelto = [int(i) for i in diaDevuelto]
    fechaEsperadaDeDevolucion = [int(i) for i in fechaEsperadaDeDevolucion]
    fine = calculateFine(diaDevuelto, fechaEsperadaDeDevolucion)
    print(str(fine))


    
