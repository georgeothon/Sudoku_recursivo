import time


def LeiaMatriz(NomeArquivo):
 
    try:
        arq = open(NomeArquivo, "r")
    except:
        return [] 
 
    mat = [9 * [0] for k in range(9)]
    i = 0
    for linha in arq:
        v = linha.split()


        for j in range(len(v)):
            mat[i][j] = int(v[j])

        i = i + 1

    arq.close()
    return mat


    
def ImprimaMatriz (Mat):

    for i in range(len(Mat)):
        for j in range(len(Mat[i])):
            if j == 8:
                print(Mat[i][j])
            else:
                print(Mat[i][j],end=' ')
     

def ProcuraElementoLinha (Mat, L, d):

    if d not in Mat[L]:
        return (-1)

    else:
        for coluna in range(len(Mat[L])):
            if Mat[L][coluna] == d :
                return coluna



def ProcuraElementoColuna (Mat, C, d): 

    for linha in range(9):
        if Mat[linha][C] == d:
            return linha  
    return -1

def ProcuraElementoQuadrado(Mat, L, C, d ):
    #Encontrar primeira casa do quadrado
    
    LinhaQuadrado = L//3
    ColunaQuadrado = C//3

    for i in range(3):
        for j in range(3):
            if Mat[ 3*LinhaQuadrado + i][ 3*ColunaQuadrado + j] == d :
                return (i,j)

    return (-1,-1)

def TestaMatrizPreenchida(Mat):

    AuxiliarColuna = []
    AuxiliarQuadrado = []
    
    for i in range(9):
        for j in range(9):


            if j != 8 :
                if Mat[i][j] in Mat[i][j+1:]:
                    return False            
                

            LinhaElemento = ProcuraElementoColuna(Mat,i,j+1)

            if LinhaElemento != -1 :
                if Mat[LinhaElemento][i] in AuxiliarColuna:
                    return False
                else:
                    AuxiliarColuna.append(Mat[LinhaElemento][i])

            for k in range(3):
                for l in range(3):
                    if Mat[ 3*(i//3) + k][ 3*(j//3) + l] != 0 :
                        if Mat[ 3*(i//3) + k][ 3*(j//3) + l] in AuxiliarQuadrado:
                            
                            return False
                        else:
                            AuxiliarQuadrado.append(Mat[ 3*(i//3) + k][ 3*(j//3) + l])

    return True


            

def TestaMatrizLida(Mat):

    AuxiliarColuna = []
    AuxiliarQuadrado = []
    
    for i in range(9):
        for j in range(9):

    # Testa se tem apenas numeros de 0 a 9
    
            if Mat[i][j] not in range(10):

                return False

            if Mat[i][j] != 0:
                if j != 8 :
                    if Mat[i][j] in Mat[i][j+1:]:

                        return False            
                

                LinhaElemento = ProcuraElementoColuna(Mat,i,j+1)

                if LinhaElemento != -1 :
                    if Mat[LinhaElemento][i] in AuxiliarColuna:

                        return False
                    else:
                        AuxiliarColuna.append(Mat[LinhaElemento][i])
                        

                for k in range(3):
                    for l in range(3):
                        if Mat[ 3*(i//3) + k][ 3*(j//3) + l] != 0 :
                            if Mat[ 3*(i//3) + k][ 3*(j//3) + l] in AuxiliarQuadrado:
                                return False
                            else:
                                AuxiliarQuadrado.append(Mat[ 3*(i//3) + k][ 3*(j//3) + l])
                AuxiliarQuadrado = []
        AuxiliarColuna = []     
    return True
  
def Sudoku(Mat,lin=0,col=0):
    
    global contador

    if Mat[lin][col] == 0:
        for d in range(1,10):
            if ProcuraElementoLinha(Mat,lin,d) == -1 and ProcuraElementoColuna(Mat,col,d) == -1 and ProcuraElementoQuadrado(Mat,lin,col,d) == (-1,-1):
                Mat[lin][col] = d
                
                if col < 8:
                    Sudoku(Mat,lin,col+1)
                elif lin < 8:
                    Sudoku(Mat,lin+1,col=0)
                else:
                    ImprimaMatriz(Mat)
                    TesteFinal = TestaMatrizPreenchida(Mat)
                    if True:
                        print("* * * Matriz Completa e consistente * * *")
                        contador += 1

                Mat[lin][col] = 0
                
    else:
        
        if col < 8:
            Sudoku(Mat,lin,col+1)
        elif lin < 8:
            Sudoku(Mat,lin+1,col=0)
        else:
            ImprimaMatriz(Mat)
            TesteFinal = TestaMatrizPreenchida(Mat)
            if True:
                print("* * * Matriz Completa e consistente * * *")
                contador += 1
    
            Mat[lin][col] = 0
    
    

while True:
    

    NomeArquivo = input("Digite o nome do arquivo que contem o sudoku: ")
    tempo1 = time.clock()
    Mat = LeiaMatriz(NomeArquivo)
    contador = 0
    
    if Mat != False:
        
        print("* * * Matriz Inicial * * *")
        ImprimaMatriz(Mat)
    
    TesteInicial = TestaMatrizLida(Mat)

    if TesteInicial == True:

        print("* * * Matriz Completa * * *")
        Sudoku(Mat)

    tempo2 = time.clock()
    print("* * * - Tempo decorrido = ",tempo2 - tempo1)
    print("* * * -",contador, "soluções para esta matriz * * *")


























