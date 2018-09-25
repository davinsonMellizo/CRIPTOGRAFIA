class CifradoCesar:
    def __init__(self, palabra, key):
        self.__palabra = palabra
        self.__key = key
        self.__palabraEncriptada = ''
        self.__alfabeto = '' #el alfabeto tambien lo pueden poner manualmente xd
        self.__generar_alfabeto() # esta fun. genere al alfabeto de la <a-z>
    def __generar_alfabeto(self):
        ##      ___genera alfabeto original___
        i=97  ## es el valor decimal de los caracteres ASCII
        while i<=122:
            self.__alfabeto+=(chr(i))
            if chr(i)=="n":
                self.__alfabeto+="ñ"
            i+=1
    def encriptar(self): # formula [Cesar = (LETRA + KEY) % TAM_ALFABETO]
        posPalabra = 0
        for i in self.__palabra:
            if i == ' ':
                self.__palabraEncriptada += ' '
            else:
                posPalabra = self.__alfabeto.find(i)
                modulo = (posPalabra+self.__key)%len(self.__alfabeto)
                self.__palabraEncriptada += self.__alfabeto[modulo]
        return self.__palabraEncriptada
        
        
        
        