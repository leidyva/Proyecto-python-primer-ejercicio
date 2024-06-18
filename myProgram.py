import math

def calculate_square_root():
    number=float(input("Ingresa un número para calcular su raíz cuadrada: "))
    if number < 0:
        print("No se puede calcular la raíz cuadrada de un número negativo.")
        return
    
    square_root = math.sqrt(number)
    print(f"La raíz cuadrada de {number} es {square_root}")
calculate_square_root()