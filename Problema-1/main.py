def juego():
    try:
        numero_usuario = input("Ingrese un numero p+ ")
        if not numero_usuario.isdigit() or len(numero_usuario) < 10:
            raise ValueError("El número debe ser positivo y tener al menos 10 dígitos.")
        
        while len(numero_usuario) >= 4:
            x, y = int(numero_usuario[:2]), int(numero_usuario[2:4])
            
            while x >= 10:
                x = sum(int(digit) for digit in str(x))
            
            while y >= 10:
                y = sum(int(digit) for digit in str(y))
            
            if x > y:
                print(f"Carro_X: {int(numero_usuario[:2])} -> {x}, Carro_Y: {int(numero_usuario[2:4])} -> {y}, Ganador: Carro_X")
            elif x < y:
                print(f"Carro_X: {int(numero_usuario[:2])} -> {x}, Carro_Y: {int(numero_usuario[2:4])} -> {y}, Ganador: Carro_Y")
            else:
                print(f"Carro_X: {int(numero_usuario[:2])} -> {x}, Carro_Y: {int(numero_usuario[2:4])} -> {y}, Empate: Ambos avanzan")
            
            numero_usuario = numero_usuario[4:]
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    juego()
