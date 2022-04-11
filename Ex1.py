def inputValuesAndVerify():
    values = input("Introduceti un sir format dintr-un numar multiplu de 7 caractere binare: ").split()
    if len(values) == 1:
        print("Valorile nu reprezinta un sir format dintr-un numar multiplu de 7 caractere binare, incercati din nou.")
        return 0
    for x in values:
        if len(x) != 7:
            print("Valorile nu reprezinta un sir format dintr-un numar multiplu de 7 caractere binare, incercati din nou.")
            return 0
    for i in range(len(values)):
        for j in range(7):
            if not(values[i][j] == "0" or values[i][j] == "1"):
                print("Valorile nu reprezinta un sir format dintr-un numar multiplu de 7 caractere binare, incercati din nou.")
                return 0
    print("Matricea arata astfel: \n")
    for x in values:
        print(x)

    return values

def addTwoMoreColumnsAndARow(matrice):
    for i in range(len(matrice)):
        matrice[i] += ' '
    newEmptyRow = ['']
    matrice.extend(newEmptyRow)
    return matrice

def createLastRow(matrice):
    checkParity = 0
    for i in range(7):
        for j in range(len(matrice)-1):
            checkParity += int(matrice[j][i])
        if checkParity % 2 == 0:
            matrice[-1] += '0'
        else:
            matrice[-1] += '1'
        checkParity = 0
    matrice[-1] += ' '
    return matrice

def createLastColumn(matrice):
    checkParity = 0
    for i in range(len(matrice)):
        for j in range(7):
            checkParity += int(matrice[i][j])
        if checkParity % 2 == 0:
            matrice[i] += '0'
        else:
            matrice[i] += '1'
        checkParity = 0

    return matrice

def ShowMatrix(matrice):
    for i in range(len(matrice)-1):
        print(matrice[i])
    print('')
    print(matrice[-1])

def bitiDeParitateBidimensionala():
    valoriIntroduse=0
    while(valoriIntroduse==0):
        valoriIntroduse = inputValuesAndVerify()

    valoriIntroduse = addTwoMoreColumnsAndARow(valoriIntroduse)
    valoriIntroduse = createLastRow(valoriIntroduse)
    valoriIntroduse = createLastColumn(valoriIntroduse)
    print('\n\nRezultatul final:\n\n')
    ShowMatrix(valoriIntroduse)

bitiDeParitateBidimensionala()
