#arbolUno="Guayacan"
#arbolDos="Ceiba"
#arbolTres="Laurel"
#ar0bolCuatro="Manzanillo"
#asi no

#Toda lista se debe escribir en plural
arboles=['ceiba','yarumo','manzano','guayacan']

#lista de municpios
#un arreglo o lista puede guardar diferentes tipos de datos en python

municipios=['Medellin','titiribi','Carolina del principe']

hectareaSembradas=[2500,500,1200]

lluviasMayoresA500=[False,True,True]

#Recorriendo un arreglo...
#Acceder  de FORMA DINAMICA al contenido de un arreglo
#Para recorrerlo debo utilizar un ciclo o bucle o loop

#ciclo while (mientras)
#Los contadores son variables auixiliares, quien vigila la ejecucuion y pone los frenos, arrancando en 0
'''contador=0
while contador<10 :
    contador=contador+1
    print("Estoy triunfando...")'''


#un For normal: for(contador=i. i<10, i=i+1){....}
#ciclo For (Para) en python
'''or variableiteradora in range(1,11):
    print(variableiteradora)'''

#Recorrer dinamicamente un arreglo usando un FOREACH (Para cada uno) En una bolsa de marcadores saca un solo marcador
for arbol in arboles:
    print(arbol)

for municipio in municipios:
    print(municipio)