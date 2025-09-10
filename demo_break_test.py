"""
Archivo de demostración para mostrar cómo romper intencionalmente una prueba
Este archivo NO debe ser incluido en el repositorio final, solo es para demostración
"""

# Para demostrar que los tests fallan cuando se rompe la funcionalidad,
# puedes descomentar la siguiente línea en test_math_lib.py:

# self.assertEqual(square(2), 5)  # Esto debería ser 4, no 5

# O puedes modificar temporalmente la función square en math_lib.py:
# def square(n):
#     if not isinstance(n, (int, float)):
#         raise TypeError("El argumento debe ser un número")
#     return n * n + 1  # Agregar +1 para romper la función

# Esto hará que los tests fallen y demuestre que el sistema de CI funciona correctamente.

