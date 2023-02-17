# Programa para verificar un numero si es par o impar
# input
x = int(input("digite un numero"))
# processing  
r = x%2
# output
if r==0:
    msj="PAR"
else:
    msj="IMPAR"

print("EL NUMERO " + str(x) + " es " + msj )