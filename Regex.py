import re

opcion = 0
while opcion != 6:

    #print(diccionario)

    print("\nSelecciona una opción")
    print("1.Buscar palabra\n"
         +"2.Buscar número\n"
         +"3.Palabras que inicien con Mayúscula\n"
         +"4.Palabras que finalicen con vocal\n"
         +"5.Encontrar números\n"
         +"6.Salir")
    opcion = int(input("Ingresa una opción: "))

    if opcion == 1:
        texto = "Curso de Python 3 con ejemplos"
        print(texto, end="\n")
        regex = input("Ingresa la palabra que deseas encontrar: ")
        if re.search(regex, texto):
            print("La palabra \"" + regex + "\" si se encuentra en el texto")
        else:
            print("Palabra no encontrada")
    elif opcion == 2:
        texto = input("Escribe un texto: ")
        regex = "\d+"
        if re.search(regex, texto):
            print("Si hay números en el texto")
        else:
            print("No hay números en el texto")
    elif opcion == 3:
        filename = "loremipsum.txt"
        textFile = open(filename, "r")
        regex = "[A-Z][a-z]+"
        reg = re.compile(regex)
        for line in textFile:
            lista = reg.findall(line)
            print(lista)
        textFile.close()
    elif opcion == 4:
        filename = "loremipsum.txt"
        textFile = open(filename, "r")
        regex = "[A-Za-z]+"
        reg = re.compile(regex)
        for line in textFile:
            lista = reg.findall(line)
            regex = "[A-Za-z]+[aeiou]$"
            for elemento in lista:
                if re.search(regex, elemento):
                    print(elemento)
        textFile.close()
    elif opcion == 5:
        filename = "loremipsum.txt"
        textFile = open(filename, "r")
        regex = "[0-9]{2,}"
        reg = re.compile(regex)
        for line in textFile:
            lista = reg.findall(line)
            print(lista)
        textFile.close()
    elif opcion == 6:
        print("¡Finalizado con exito!")
    else:
        print("\n¡La opción seleccionada es incorrecta!")   