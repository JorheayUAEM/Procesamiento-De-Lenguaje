from collections import Counter

def countVocales(path):
    """
    Método que cuenta las vocales incluidas en un archivo con extensión .txt    
    Args:
        - path (str): Ruta del archivo a analizar 
    """
    with open(path, encoding='utf-8') as f:
        letras = f.read().replace('\n', '')
    contador = 0
    for letra in letras:
        if letra.lower() in "aeiouÁÉÍÓÚáéíóú":
            contador += 1
    print(f"La cantidad de vocales es: {contador}")


def countPalabras(path):
    """
    Método que cuenta las palabras totales en un archivo con extensión .txt    
    Args:
        - path (str): Ruta del archivo a analizar 
    """
    palabras = 0
    with open(path,'r') as file: 
        for line in file: 
            for word in line.split(): 
                palabras += 1
    print(f"La cantidad de palabras es: {palabras}")


def mostCommon(path):
    """
    Método que identifica la palabra más frecuente en un archivo con extensión .txt    
    Args:
        - path (str): Ruta del archivo a analizar 
    """
    with open(path, encoding='utf-8') as f:
        letras = f.read().replace('\n', '')
    palabras = letras.split()
    contador = Counter(palabras)
    mas_frecuente = contador.most_common()[0][0]
    print(f"La palabra mas frecuente es: {mas_frecuente}")



#Ingresar la ruta del archivo con extensión ".txt" en los paréntesis de los siguientes dos métodos
#Método cuenta vocales
countVocales("Texto.txt")
#Método cuenta palabras
countPalabras("Texto.txt")
#Metodo para identificar la palabra mas frecuente
mostCommon("Texto.txt")