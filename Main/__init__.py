import sys
from Cesar import CifradoCesar as CF
import menu
def main():
	posArchEn=3
	posArchSa=4
	if len(sys.argv)<2:
		menu.algoritmos()
		posArchEn=0
		posArchSa=0
	else:
		if sys.argv[posArchEn-2]=="-jc" and sys.argv[posArchSa-2]=="-a":
			menu.ayudacesar()
		else:
			if sys.argv[posArchEn-2]=="-jc" and sys.argv[posArchSa-2]=="-c":
				print("Procesando...")
				print()
				archivo = open(sys.argv[3], "r")
				texto=archivo.read()
				archivo.close() 
				cf = CF(texto, 3)
				f = open (sys.argv[4],'w')
				f.write(cf.encriptar())
				f.close()
				menu.fincesar()
			else:
				if sys.argv[posArchEn-2]=="-jc" and sys.argv[posArchSa-2]=="-d":
					print("Procesando des...")
					print()
					archivo = open(sys.argv[3], "r")
					texto=archivo.read()
					archivo.close() 
					cf = CF(texto, -3)
					f = open (sys.argv[4],'w')
					f.write(cf.encriptar())
					f.close()
					menu.fincesar()
	    
if __name__ == '__main__':
    main()

    