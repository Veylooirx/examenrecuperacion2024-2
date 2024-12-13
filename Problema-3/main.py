def limpiar_texto(texto):

    return ''.join(c for c in texto if c.isalpha() or c.isspace())

def procesar_archivo(nombre_archivo):

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for renglon in archivo:
                renglon_limpio = limpiar_texto(renglon)
                
                palabras = renglon_limpio.split()
                
                palabras_ordenadas = sorted(palabras, key=lambda palabra: [*palabra.lower()])
                
                print(" ".join(palabras_ordenadas))

    except FileNotFoundError:
        print("no encuentro tu cochinero")
    except Exception as e:
        print(f"valio mouser {e}")

if __name__ == "__main__":
    nombre_archivo = "texto.txt"  
    procesar_archivo(nombre_archivo)
