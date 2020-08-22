
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
    Tweets = {}
    with open(file, 'r',encoding=('UTF-8-sig')) as f:
        Tweets = json.load(f)
    return(Tweets)

def calcularSentimiento(sentimientos,tweet):
    valor = 0
    texto = tweet.split(" ")
    for i in texto:
        if (not "http"in i and not "@:"in i):
            if(sentimientos.get(i)):
                valor = valor + int(sentimientos.get(i))
    return valor



if __name__ == '__main__':
    import os
    import json
    path = input("Ruta de la carpeta donde están los archivos Input:")
    #path = r"C:\Users\juanx\Downloads\CasoPractico"
    archivo=input("Nombre del archivo de sentimientos Con terminación.txt:")
    #archivo = "Sentimientos.txt"
    archivoTweets = input("Nombre del archivo de Tweets Con terminación.txt:")
    #archivoTweets = "Tweets.txt"
    sentimientos = {}
    try:
        sentimientos=leerSentimientos(path,archivo)
    except FileNotFoundError or OSError:
        print("Ruta de sentimientos no válida")
        exit()


    contador=0
    try:
        with open(archivoTweets, 'r',encoding=('UTF-8-sig')) as f:
            for i in f.readlines():
                texto=json.loads(i)
                if texto.get("text"):
                    print("Tweet: ", texto.get("text").lower(),'Sentimiento: ', calcularSentimiento(sentimientos,texto.get("text").lower()))
                    contador+=1
    except FileNotFoundError or OSError:
        print("Ruta de Tweets no válida")
        exit()



