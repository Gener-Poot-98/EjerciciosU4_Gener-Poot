import re

filename = "Regex.py"
textFile = open(filename, "r")
regex1 = "[a-z]+\d*[-|_]*[a-zA-Z]*\s="
lista_temp1 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex1, linea)
    if len(x) > 0:
        lista_temp1.append(x)

filename = "Regex.py"
textFile = open(filename, "r")
regex2 = "\d{1,}\.*[\d]*"
lista_temp2 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex2, linea)
    if len(x) > 0:
        lista_temp2.append(x)

filename = "Regex.py"
textFile = open(filename, "r")
regex3 = "[+|\-|*|/|%]"
lista_temp3 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex3, linea)
    if len(x) > 0:
        lista_temp3.append(x)

filename = "Regex.py"
textFile = open(filename, "r")
regex4 = "[>=]{2}|[<=]{2}|[!=]{2}|[>]|[<]"
lista_temp4 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex4, linea)
    if len(x) > 0:
        lista_temp4.append(x)

filename = "Regex.py"
textFile = open(filename, "r")
regex5 = "False|class|from|\Wor\W|None|continue|global|pass|True|\Wdef\W|if|raise|\Wand\W|\Wdel\W|import|return|\Was\W|elif|\Win\W|try|assert|else|\Wis\W|while|async|except|lambda|with|await|finally|nonlocal|yield|break|for|not"
lista_temp5 = []
for linea in textFile:
    linea = linea.rstrip()
    x = re.findall(regex5, linea)
    if len(x) > 0:
        lista_temp5.append(x)

opcion = True
while opcion == True:
    print("\n"+"--------------------ANALIZADOR DE PATRONES--------------------")
    print("El archivo analizado es: "+str(filename)+"\n")
    print("-------------------------EJERCICIO 1--------------------------")
    print("Las variables válidas encontradas en el archivo son:")
    print(str(lista_temp1)+"\n")
    print("-------------------------EJERCICIO 2--------------------------")
    print("Los números enteros y decimales encontrados en el archivo son:")
    print(str(lista_temp2)+"\n")
    print("-------------------------EJERCICIO 3--------------------------")
    print("Los operadores aritméticos encontrados en el archivo son:")
    print(str(lista_temp3)+"\n")
    print("-------------------------EJERCICIO 4--------------------------")
    print("Los operadores relacionales encontrados en el archivo son:")
    print(str(lista_temp4)+"\n")
    print("-------------------------EJERCICIO 5--------------------------")
    print("Las palabras reservadas encontrados en el archivo son:")
    print(str(lista_temp5)+"\n")
    print("-----------------------DATOS DEL ALUMNO-----------------------")
    print("Nombre: Gener Emmanuel Poot Can")
    print("Semestre y grupo: 5 Semestre | Grupo A"+"\n")
    res = input("Ingrese el comando [exit] para salir: ")
    if res == "[exit]":
        opcion = False
    print("Hasta luego, vuelva pronto")