# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def leerSentimientos(path,file):
    os.chdir(path)
    #print(os.getcwd())
    sentimientos = open(file)
    valores = {}
    for  linea in sentimientos:
        termino,valor=linea.split("\t")
        valores[termino]=int(valor)
    return valores

def leerTweets(file):
    data = {}
    import json
    import pandas as pd

    with open(file, 'r') as f:
        for l in f.readlines():
            if not l.strip():  # skip empty lines
                continue

            Tweets = json.loads(l)
            return(Tweets)

if __name__ == '__main__':
    import os
    path = input("Ruta de la carpeta donde está el archivo de sentimientos:")
    archivo=input("Nombre del archivo de sentimientos Con terminación.txt:")
    archivoTweets = input("Nombre del archivo de Tweets Con terminación.txt:")
    sentimientos = {}
    tweets = {}
    try:
        sentimientos=leerSentimientos(archivo,path)
        tweets = leerTweets(archivoTweets)
    except FileNotFoundError or OSError:
        print("Ruta no válida")



