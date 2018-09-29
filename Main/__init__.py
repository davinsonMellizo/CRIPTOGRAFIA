import sys
from Cesar import CifradoCesar as CF
from polybios import CifradoPolybios as PB
import menu
#METO QUE LLAMA LA FUNCION DE CIFRAR CON EL METODO DE CESAR
def cifrarcesar():
	print("Procesando...")
	print()
	archivo = open(sys.argv[3], "r")
	texto=archivo.read()
	archivo.close() 
	cf = CF(texto, 3)
	f = open (sys.argv[4],'w')
	f.write(cf.cifrar())
	f.close()
	menu.fin()
#METO QUE LLAMA LA FUNCION DE DESCIFRAR CON EL METODO DE CESAR
def descifrarcesar():
	print("Procesando...")
	print()
	archivo = open(sys.argv[3], "r")
	texto=archivo.read()
	archivo.close() 
	cf = CF(texto, -3)
	f = open (sys.argv[4],'w')
	f.write(cf.cifrar())
	f.close()
	menu.fin()
#METO QUE LLAMA LA FUNCION DE CIFRAR CON EL METODO POLYBIOS
def cifrarpolybios(alfabeto):
	print("Procesando...")
	print()
	archivo = open(sys.argv[4], "r")
	texto=archivo.read()
	archivo.close()
	pb = PB(texto,alfabeto)
	f = open (sys.argv[5],'w')
	f.write(pb.cifrar())
	f.close()
	menu.fin()
#METO QUE LLAMA LA FUNCION DE DESCIFRAR CON EL METODO DE POLYBIOS
def descifrarpolybios(alfabeto):
	print("Procesando...")
	print()
	archivo = open(sys.argv[4], "r")
	texto=archivo.read()
	archivo.close()
	pb = PB(texto,alfabeto)
	f = open (sys.argv[5],'w')
	f.write(pb.descifrar())
	f.close()
	menu.fin()

def main():
	#SI SOLO SE EJECUTA EL PROGRAMA MUESTRA EL MENU
	if len(sys.argv)<=1:
		menu.algoritmos()
	else:
		#si es igual a tres puede ser una ayuda
		if(len(sys.argv)==3):
			if sys.argv[1]=="-jc" and sys.argv[2]=="-a":
				menu.ayudacesar()
			if sys.argv[1]=="-pb" and sys.argv[2]=="-a":
				menu.ayudacesar()
		#si es igual a 5 puede ser julio cesar...	
		if (len(sys.argv)==5):
			if sys.argv[1]=="-jc" and sys.argv[2]=="-c":
				cifrarcesar()
			if sys.argv[1]=="-jc" and sys.argv[2]=="-d":
				descifrarcesar()
		#si es igual a 6 puede ser polybios
		if(len(sys.argv)==6):
			if sys.argv[1]=="-pb" and sys.argv[2]=="-c" and sys.argv[3]=="-n":
				cifrarpolybios("n")
			if sys.argv[1]=="-pb" and sys.argv[2]=="-c" and sys.argv[3]=="-l":
				cifrarpolybios("l")
			if sys.argv[1]=="-pb" and sys.argv[2]=="-d" and sys.argv[3]=="-n":
				descifrarpolybios("n")
			if sys.argv[1]=="-pb" and sys.argv[2]=="-d" and sys.argv[3]=="-l":
				descifrarpolybios("l")

		
#METODO QUE INICIA EL PROGRAMA		
if __name__ == '__main__':
    main()

    