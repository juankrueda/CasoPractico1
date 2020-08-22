
def leerSentimientos(path,file):
    os.chdir(path)
    print(os.getcwd())
    sentimientos = open(file)
    valores = {}
    for  linea in sentimientos:
        termino,valor=linea.split("\t")
        valores[termino]=int(valor)
    return valores

def leerTweets(file):
    data = {}

    with open("Tweets.txt", 'r') as f:
        for l in f.readlines():
            if not l.strip():  # skip empty lines
                continue

            Tweets = json.loads(l)
            return(Tweets)

if __name__ == '__main__':
    import os
    import json
    #path = input("Ruta de la carpeta donde están los archivos Input:")
    path = r"C:\Users\juanx\Downloads\CasoPractico"
    #archivo=input("Nombre del archivo de sentimientos Con terminación.txt:")
    archivo = "Sentimientos.txt"
    #archivoTweets = input("Nombre del archivo de Tweets Con terminación.txt:")
    archivoTweets = " Tweets.txt"
    sentimientos = {}
    tweets = {}
    try:
        sentimientos=leerSentimientos(path,archivo)
    except FileNotFoundError or OSError:
        print("Ruta de sentimientos no válida")


    try:
        tweets = leerTweets(archivoTweets)
    except FileNotFoundError or OSError:
        print("Ruta de Tweets no válida")

    print (tweets)

