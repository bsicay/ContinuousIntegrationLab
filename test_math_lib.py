"""
Pruebas unitarias para la librería de matemática básica
"""

import unittest
import math
from math_lib import square, factorial, is_prime, gcd, lcm


class TestMathLib(unittest.TestCase):
    """Clase de pruebas para las funciones matemáticas"""

    def test_square_happy_path(self):
        """Pruebas exitosas para la función square"""
        # Caso 1: Número entero positivo
        self.assertEqual(square(5), 25)
        # Caso 2: Número decimal
        self.assertEqual(square(2.5), 6.25)
        # Caso 3: Número negativo
        self.assertEqual(square(-3), 9)
        # Caso 4: Cero
        self.assertEqual(square(0), 0)

    def test_square_error_cases(self):
        """Pruebas de error para la función square"""
        # Caso de error: string
        with self.assertRaises(TypeError):
            square("5")
        # Caso de error: lista
        with self.assertRaises(TypeError):
            square([1, 2, 3])

    def test_factorial_happy_path(self):
        """Pruebas exitosas para la función factorial"""
        # Caso 1: Número pequeño
        self.assertEqual(factorial(3), 6)
        # Caso 2: Número más grande
        self.assertEqual(factorial(5), 120)
        # Caso 3: Cero y uno
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_error_cases(self):
        """Pruebas de error para la función factorial"""
        # Caso de error: número negativo
        with self.assertRaises(ValueError):
            factorial(-1)
        # Caso de error: tipo incorrecto
        with self.assertRaises(TypeError):
            factorial(3.5)
        # Caso de error: string
        with self.assertRaises(TypeError):
            factorial("5")

    def test_is_prime_happy_path(self):
        """Pruebas exitosas para la función is_prime"""
        # Caso 1: Números primos
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(97))
        # Caso 2: Números no primos
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(100))

    def test_is_prime_error_cases(self):
        """Pruebas de error para la función is_prime"""
        # Caso de error: tipo incorrecto
        with self.assertRaises(TypeError):
            is_prime(3.5)
        # Caso de error: string
        with self.assertRaises(TypeError):
            is_prime("7")

    def test_gcd_happy_path(self):
        """Pruebas exitosas para la función gcd"""
        # Caso 1: Números positivos
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(15, 25), 5)
        # Caso 2: Con números negativos
        self.assertEqual(gcd(-12, 8), 4)
        self.assertEqual(gcd(12, -8), 4)
        # Caso 3: Números coprimos
        self.assertEqual(gcd(7, 11), 1)
        # Caso 4: Uno de los números es cero
        self.assertEqual(gcd(5, 0), 5)

    def test_gcd_error_cases(self):
        """Pruebas de error para la función gcd"""
        # Caso de error: tipos incorrectos
        with self.assertRaises(TypeError):
            gcd(3.5, 5)
        with self.assertRaises(TypeError):
            gcd(5, "3")

    def test_lcm_happy_path(self):
        """Pruebas exitosas para la función lcm"""
        # Caso 1: Números positivos
        self.assertEqual(lcm(12, 8), 24)
        self.assertEqual(lcm(15, 25), 75)
        # Caso 2: Con números negativos
        self.assertEqual(lcm(-12, 8), 24)
        self.assertEqual(lcm(12, -8), 24)
        # Caso 3: Números coprimos
        self.assertEqual(lcm(7, 11), 77)
        # Caso 4: Números iguales
        self.assertEqual(lcm(5, 5), 5)

    def test_lcm_error_cases(self):
        """Pruebas de error para la función lcm"""
        # Caso de error: tipos incorrectos
        with self.assertRaises(TypeError):
            lcm(3.5, 5)
        with self.assertRaises(TypeError):
            lcm(5, "3")
        # Caso de error: uno de los números es cero
        with self.assertRaises(ValueError):
            lcm(5, 0)
        with self.assertRaises(ValueError):
            lcm(0, 5)

    def test_break_functionality(self):
        """
        Prueba para demostrar que los tests fallan cuando se rompe la funcionalidad.
        Esta prueba está diseñada para fallar y demostrar que el sistema de CI funciona.
        """
        # Esta línea está intencionalmente mal para demostrar que los tests fallan
        self.assertEqual(square(2), 5)  # Esto debería ser 4, no 5


if __name__ == '__main__':
    unittest.main()
