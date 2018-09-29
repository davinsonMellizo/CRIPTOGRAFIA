class CifradoPolybios:
    #CONSTRUCTOR DE LA CLASE
    def __init__(self, palabra, alfabetoP):
        self.__palabra = palabra
        self.__palabraEncriptada = ''
        self.__alfabeto=[]
        if alfabetoP=="l":
            self.__alfabetoC =  ["A","B","C","D","E"]
        else:
            self.__alfabetoC =  ["1","2","3","4","5"]
        self.__generar_alfabeto()
    #METODO QUE GENERA EL ALFABETO
    def __generar_alfabeto(self):

        i=97  
        while i<=122:
            if chr(i)=="j":
                i+=1
            self.__alfabeto+=(chr(i))
            i+=1
    #METODO POLYBIOS PARA CIFRAR
    def cifrar(self): 
        for i in self.__palabra:
            if(i!="\n"):#SI NO ES UN ENTER SE CONTUNIA
                if i == ' ':
                    self.__palabraEncriptada += ' '
                else:
                    pos=self.__alfabeto.index(i)+1#OBTIENE LA POSICION DEL CARACTER EN EL ALFABETO
                    #SACAMOS LAS POSICIONES EN LA MATRIZ
                    if pos%5==0:
                        posHor=4#POSICION DE COLUMNA EN LA MATRIZ
                        posVer=int(pos/5)-1#POSICION DE FILA EN LA MATRIZ
                    else:
                        posHor=pos%5-1#POSICION DE COLUMNA EN LA MATRIZ
                        posVer=int(pos/5)#POSICION DE FILA EN LA MATRIZ
                    #SACAMOS LAS DOS LETRAS QUE CIFRAN
                    cifra=self.__alfabetoC[posVer]+self.__alfabetoC[posHor]
                    #GUARDAMOS LAS DOS LETRAS
                    self.__palabraEncriptada +=cifra
        return self.__palabraEncriptada
    #METODO POLYBIOS PARA DESCIFRAR
    def descifrar(self): 
        posLetra=int(2);
        primera=""
        for i in self.__palabra:
            if posLetra%2==0:#PARA SACAR UN PAR DE SIMBOLOS
                primera=i
            else:
                #SI YA ESTAN LOS DOS SIMBOLOS SE SACA LA LETRA DEL LA MATRIZ
                posVer=self.__alfabetoC.index(primera)#POSICION EN LAS COLUMNAS
                posHor=self.__alfabetoC.index(i)+1#POSICION EN LAS FILAS
                posEnAlfabeto=posHor+posVer*5-1#POSICION EN EL ALFABETO
                #SE GUARDA LA LETRA DESCIFRADA
                self.__palabraEncriptada+=self.__alfabeto[posEnAlfabeto]
            posLetra+=1
        return self.__palabraEncriptada
                
        
        
        
        
        