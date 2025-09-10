# Configuración de Branch Protection Rules

Para que los merge estén completamente bloqueados cuando los tests fallan, debes configurar las **Branch Protection Rules** en GitHub:

## Pasos para Configurar:

1. **Ve a tu repositorio en GitHub**
2. **Settings** → **Branches**
3. **Add rule** o **Add branch protection rule**
4. **Branch name pattern**: `main`
5. **Configuración recomendada**:

### ✅ Opciones Obligatorias:
- **Require a pull request before merging**
- **Require status checks to pass before merging**
- **Require branches to be up to date before merging**

### ✅ Status Checks Requeridos:
- `test` (nombre del job en nuestro workflow)

### ✅ Opciones Adicionales Recomendadas:
- **Require conversation resolution before merging**
- **Require signed commits**
- **Restrict pushes that create files larger than 100 MB**

## Resultado:
Con esta configuración, **NO se podrá hacer merge** a menos que:
- ✅ Todos los tests pasen
- ✅ No haya errores de linting
- ✅ El PR tenga al menos una aprobación (opcional)
- ✅ La rama esté actualizada con main

## Verificación:
Para probar que funciona:
1. Crea un PR con tests que fallen
2. Intenta hacer merge → Debería estar bloqueado
3. Arregla los tests
4. Intenta hacer merge → Debería permitir el merge
