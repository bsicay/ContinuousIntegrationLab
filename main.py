#!/usr/bin/env python3
"""
Demo de la librería de matemática básica
"""

from math_lib import square, factorial, is_prime, gcd, lcm


def demo_square():
    """Demostración de la función square"""
    print("=" * 50)
    print("Función square(n)")
    print("=" * 50)
    
    test_cases = [5, 2.5, -3, 0, 10]
    
    for num in test_cases:
        try:
            result = square(num)
            print(f"square({num}) = {result}")
        except Exception as e:
            print(f"square({num}) = ERROR: {e}")
    
    print()


def demo_factorial():
    """Demostración de la función factorial"""
    print("=" * 50)
    print("Función factorial(n)")
    print("=" * 50)
    
    test_cases = [0, 1, 3, 5, 7, 10]
    
    for num in test_cases:
        try:
            result = factorial(num)
            print(f"factorial({num}) = {result}")
        except Exception as e:
            print(f"factorial({num}) = ERROR: {e}")
    
    # Casos de error
    error_cases = [-1, 3.5, "5"]
    print("\nCasos de error:")
    for num in error_cases:
        try:
            result = factorial(num)
            print(f"factorial({num}) = {result}")
        except Exception as e:
            print(f"factorial({num}) = ERROR: {e}")
    
    print()


def demo_is_prime():
    """Demostración de la función is_prime"""
    print("=" * 50)
    print("Función is_prime(n)")
    print("=" * 50)
    
    test_cases = [1, 2, 3, 4, 5, 15, 17, 25, 29, 97, 100]
    
    for num in test_cases:
        try:
            result = is_prime(num)
            status = "PRIMO" if result else "NO PRIMO"
            print(f"is_prime({num}) = {result} {status}")
        except Exception as e:
            print(f"is_prime({num}) = ERROR: {e}")
    
    print()


def demo_gcd():
    """Demostración de la función gcd"""
    print("=" * 50)
    print("Función gcd(a, b)")
    print("=" * 50)
    
    test_cases = [
        (12, 8), (15, 25), (7, 11), (5, 0), 
        (-12, 8), (12, -8), (100, 50), (17, 13)
    ]
    
    for a, b in test_cases:
        try:
            result = gcd(a, b)
            print(f"gcd({a}, {b}) = {result}")
        except Exception as e:
            print(f"gcd({a}, {b}) = ERROR: {e}")
    
    print()


def demo_lcm():
    """Demostración de la función lcm"""
    print("=" * 50)
    print("Función lcm(a, b)")
    print("=" * 50)
    
    test_cases = [
        (12, 8), (15, 25), (7, 11), (5, 5),
        (-12, 8), (12, -8), (100, 50), (17, 13)
    ]
    
    for a, b in test_cases:
        try:
            result = lcm(a, b)
            print(f"lcm({a}, {b}) = {result}")
        except Exception as e:
            print(f"lcm({a}, {b}) = ERROR: {e}")
    
    # Casos de error
    error_cases = [(5, 0), (0, 5), (3.5, 5), (5, "3")]
    print("\nCasos de error:")
    for a, b in error_cases:
        try:
            result = lcm(a, b)
            print(f"lcm({a}, {b}) = {result}")
        except Exception as e:
            print(f"lcm({a}, {b}) = ERROR: {e}")
    
    print()


def demo_interactive():
    """Demo interactivo donde el usuario puede probar las funciones"""
    print("=" * 50)
    print("INTERACTIVO")
    print("=" * 50)
    
    while True:
        print("\nSelecciona una función para probar:")
        print("1. square(n)")
        print("2. factorial(n)")
        print("3. is_prime(n)")
        print("4. gcd(a, b)")
        print("5. lcm(a, b)")
        print("0. Salir")
        
        choice = input("\nIngresa tu opción (0-5): ").strip()
        
        if choice == "0":
            print("¡Hasta luego!")
            break
        elif choice == "1":
            try:
                n = float(input("Ingresa un número: "))
                result = square(n)
                print(f"square({n}) = {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "2":
            try:
                n = int(input("Ingresa un número entero: "))
                result = factorial(n)
                print(f"factorial({n}) = {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            try:
                n = int(input("Ingresa un número entero: "))
                result = is_prime(n)
                status = "es primo" if result else "no es primo"
                print(f"{n} {status}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "4":
            try:
                a = int(input("Ingresa el primer número: "))
                b = int(input("Ingresa el segundo número: "))
                result = gcd(a, b)
                print(f"gcd({a}, {b}) = {result}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "5":
            try:
                a = int(input("Ingresa el primer número: "))
                b = int(input("Ingresa el segundo número: "))
                result = lcm(a, b)
                print(f"lcm({a}, {b}) = {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Opción inválida. Intenta de nuevo.")


def main():
    """Función principal que ejecuta todas las demos"""
    print(" DEMO DE LA LIBRERÍA DE MATEMÁTICA BÁSICA")
    print("=" * 60)
    print()
    
    # Ejecutar todas las demos
    demo_square()
    demo_factorial()
    demo_is_prime()
    demo_gcd()
    demo_lcm()



if __name__ == "__main__":
    main()
