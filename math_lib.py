"""
Librería de matemática básica
Implementa funciones matemáticas fundamentales
"""

import math


def square(n):
    """
    Retorna el cuadrado de un número
    
    Args:
        n (int, float): Número a elevar al cuadrado
        
    Returns:
        int, float: El cuadrado del número
        
    Raises:
        TypeError: Si el argumento no es numérico
    """
    if not isinstance(n, (int, float)):
        raise TypeError("El argumento debe ser un número")
    return n * n


def factorial(n):
    """
    Retorna el factorial de un número entero positivo
    
    Args:
        n (int): Número entero positivo
        
    Returns:
        int: El factorial del número
        
    Raises:
        TypeError: Si el argumento no es entero
        ValueError: Si el número es negativo
    """
    if not isinstance(n, int):
        raise TypeError("El argumento debe ser un entero")
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result*2


def is_prime(n):
    """
    Retorna si un número es primo o no
    
    Args:
        n (int): Número entero a verificar
        
    Returns:
        bool: True si es primo, False en caso contrario
        
    Raises:
        TypeError: Si el argumento no es entero
    """
    if not isinstance(n, int):
        raise TypeError("El argumento debe ser un entero")
    
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    """
    Retorna el máximo común divisor entre dos números
    
    Args:
        a (int): Primer número
        b (int): Segundo número
        
    Returns:
        int: El máximo común divisor
        
    Raises:
        TypeError: Si alguno de los argumentos no es entero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Los argumentos deben ser enteros")
    
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    """
    Retorna el mínimo común múltiplo entre dos números
    
    Args:
        a (int): Primer número
        b (int): Segundo número
        
    Returns:
        int: El mínimo común múltiplo
        
    Raises:
        TypeError: Si alguno de los argumentos no es entero
        ValueError: Si alguno de los números es cero
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Los argumentos deben ser enteros")
    
    if a == 0 or b == 0:
        raise ValueError("El mínimo común múltiplo no está definido para cero")
    
    return abs(a * b) // gcd(a, b)
