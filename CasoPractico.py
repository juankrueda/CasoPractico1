# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def leerSentimientos(path,file):
    os.chdir(path)
    print(os.getcwd())
    sentimientos = open(file)
    valores = {}
    for  linea in sentimientos:
        termino,valor=linea.split("\t")
        valores[termino]=int(valor)
    return(valores)



if __name__ == '__main__':
    import os
    path = input("Ruta de la carpeta donde está el archivo de sentimientos:")
    archivo=input("Nombre del archivo de sentimientos Con terminación.txt:")
    sentimientos = {}
    try:
        sentimientos=leerSentimientos(path,archivo)
    except FileNotFoundError or OSError:
        print("Ruta no válida")

