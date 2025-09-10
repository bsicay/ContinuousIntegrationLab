# Librería de Matemática Básica

Este proyecto implementa una librería de funciones matemáticas básicas con pruebas unitarias y integración continua.

## Funciones Implementadas

- `square(n)`: Retorna el cuadrado de un número
- `factorial(n)`: Retorna el factorial de un número entero positivo
- `is_prime(n)`: Retorna si un número es primo o no
- `gcd(a, b)`: Retorna el máximo común divisor entre dos números
- `lcm(a, b)`: Retorna el mínimo común múltiplo entre dos números

## Instalación

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd ContinuousIntegrationLab

# No se requieren dependencias adicionales
```

## Uso

```python
from math_lib import square, factorial, is_prime, gcd, lcm

# Ejemplos de uso
print(square(5))        # 25
print(factorial(5))     # 120
print(is_prime(17))     # True
print(gcd(12, 8))       # 4
print(lcm(12, 8))       # 24
```

## Ejecutar Pruebas

```bash
# Ejecutar todas las pruebas
python -m pytest test_math_lib.py

# O usando unittest
python test_math_lib.py
```

## Integración Continua

Este proyecto utiliza GitHub Actions para ejecutar automáticamente las pruebas unitarias en cada Pull Request. El workflow verifica que:

1. Todas las pruebas pasen exitosamente
2. No se permita hacer merge si las pruebas fallan
3. Se ejecute en cada Pull Request hacia la rama main

## Estructura del Proyecto

```
ContinuousIntegrationLab/
├── math_lib.py              # Librería principal
├── test_math_lib.py         # Pruebas unitarias
├── requirements.txt         # Dependencias (vacío)
├── README.md               # Documentación
└── .github/
    └── workflows/
        └── ci.yml          # Workflow de GitHub Actions
```
