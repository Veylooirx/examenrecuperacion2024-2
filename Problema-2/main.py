def cargar_diccionario(archivo):
    diccionario = {}
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            for linea in file:
                partes = linea.strip().split()
                if len(partes) == 2:  
                    numero, palabra = partes
                    diccionario[numero] = palabra
        return diccionario
    except FileNotFoundError:
        print("NOI hay archiv")
        return {}
    except Exception as e:
        print(f"No diccionaioa {e}")
        return {}


def decodificar(numero_entrada, diccionario):

    frase = []
    for i in range(0, len(numero_entrada), 2):  
        par = numero_entrada[i:i+2]
        if par in diccionario:  
            frase.append(diccionario[par])
        else:
            frase.append('?')  
    return ' '.join(frase)

if __name__ == "__main__":
    numero_entrada = input("Ingresa el numero de entrada: ")  
    diccionario = cargar_diccionario('texto.txt')
    
    if diccionario:  
        frase_decodificada = decodificar(numero_entrada, diccionario)
        print(frase_decodificada)
    else:
        print("Valio")
