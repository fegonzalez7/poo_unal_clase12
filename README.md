# Programación Orientada a Objetos - UNAL

## Clase 12: Excepciones 
Esperando lo inespearado

En el mundo de la programación, los errores son *inevitables*. Sin embargo, la forma de manejarlos define la **robustez** y **confiabilidad** de nuestro código. En Python, las excepciones brindan una herramienta para capturar y gestionar errores de manera efectiva.

### Definición
Las excepciones son eventos inesperados que ocurren durante la ejecución de un programa. Representan situaciones anormales que pueden impedir el correcto funcionamiento del programa. 

**Ejemplo:**
```python
# Calcular promedio
def calcular_promedio(numeros):
  total = 0
  for numero in numeros:
    total += numero
  return total / len(numeros)

promedio = calcular_promedio([1, 2, 3, "4"])
print(f"El promedio es: {promedio}")
```

```python
def calcular_promedio(numeros):
  total = 0
  for numero in numeros:
    total += numero
  return total / len(numeros)

# manejo de excepciones
try:
  promedio = calcular_promedio([1, 2, 3, "4"])
  print(f"El promedio es: {promedio}")
except TypeError:
  print("Error: Se introdujo un valor no numérico.")
```

**Explicación:** En este ejemplo, el bloque `try` contiene el código susceptible a errores. Si se produce un error de tipo `TypeError`, el bloque `except` se ejecuta, capturando la excepción y mostrando un mensaje informativo.

## Estructura `try`- `except`- `finally`
La instrucción `try` - `except` permite permite agrupar un conjunto de instrucciones en un bloque, y en caso que se levante algún error (excepción) no se detenga la ejecución de todo el programa, sino que se capture y se gestione de forma adecuada.

Lo anterior es sumamente importante, ya que se pueden tener en cuanta todos los posibles escenarios de falla y separarlos según ocurran sin que esto detenga el programa...*pretty cool*.

La estrucutura general incluye:
- **Bloque** `try`: Contiene el código que se intenta ejecutar.
- **Bloque** `except`: Se ejecuta si se produce una excepción dentro del bloque `try`. Pueden existir tantos `excepts` como tipos de excepciones se quieran procesar.
- **Bloque** `finally`: Se ejecuta siempre, sin importar si se produce una excepción o no. Es **opcional**.

**Ejemplo:**
```python
def dividir(numerador, denominador):
  return numerador / denominador

try:
  resultado = dividir(10, 0)
  print(f"El resultado de la división es: {resultado}")
except ZeroDivisionError as error:
  print(f"Error: {error}")
```

**Nota:** Cuando no se conocen las excepciones, se puede capturar de forma general y reportar el error.
```python
def dividir(numerador, denominador):
  return numerador / denominador

try:
  resultado = dividir(10, 0)
  print(f"El resultado de la división es: {resultado}")
except Exception as e:
  print(f"Error: {e}")
```

**Nota:** Es una mala práctica simplemente dejar el bloque `except` solo.
```python
def dividir(numerador, denominador):
  return numerador / denominador

try:
  resultado = dividir(10, 0)
  print(f"El resultado de la división es: {resultado}")
except:
  pass
```

### Una palabra magica `raise`
Con la instrucción `raise`se pueden levantar excepciones de forma programática, es decir que se levante una excepción deseada en el contexto adecuado.

**Ejemplo:**
```python

def obtener_elemento(lista, indice):
  if indice < 0 or indice >= len(lista):
    raise IndexError("Índice fuera de rango.")
  return lista[indice]

try:
  elemento = obtener_elemento([1, 2, 3], 4)
  print(f"El elemento en la posición 4 es: {elemento}")
except IndexError as error:
  print(f"Error: {error}")
```

### Finally
El bloque `finally` es opcional en la ejecución de un `try` - `except`, se ubica al final y lo que esté en su contexto siempre se ejecutará. Se utiliza principalmente en aquellas acciones que abren/inician un proceso y requieren cerrarlo/terminarlo.

**Ejemplo:**
```python
def abrir_archivo(ruta):
  try:
    archivo = open(ruta, "r")
    contenido = archivo.read()
    return contenido
  except FileNotFoundError as error:
    print(f"Error: {error}")
  finally:
    if archivo:
      archivo.close()

try:
  contenido_archivo = abrir_archivo("archivo.txt")
  print(f"Contenido del archivo: {contenido_archivo}")
except Exception as error:
  print(f"Error general: {error}")
```

### Excepciones comunes en python 

<table>
    <thead>
        <tr>
            <th>Excepción</th>
            <th>Explicación</th>
            <th>Manejo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>TypeError</td>
            <td>Ocurre cuando se intenta realizar una operación incompatible con los tipos de datos involucrados.</td>
            <td>Verificar los tipos de datos involucrados en la operación y asegurarse de que sean compatibles. Si es necesario, convertir los tipos de datos antes de realizar la operación.</td>
        </tr>
        <tr>
            <td>ValueError</td>
            <td>Ocurre cuando se proporciona un valor incorrecto para una operación específica.</td>
            <td>Validar los valores de entrada antes de realizar la operación. Asegurarse de que los valores sean del tipo correcto y cumplan con los requisitos específicos.</td>
        </tr>
        <tr>
            <td>NameError</td>
            <td>Ocurre cuando se hace referencia a una variable o nombre que no ha sido definido.</td>
            <td>Verificar que la variable o nombre haya sido definido antes de utilizarlo. Si es necesario, declarar la variable o nombre antes de usarla.</td>
        </tr>
        <tr>
            <td>KeyError</td>
            <td>Ocurre cuando se intenta acceder a una clave inexistente en un diccionario.</td>
            <td>Verificar si la clave existe en el diccionario antes de acceder a ella. Utilizar el método `get()` del diccionario para obtener el valor asociado a una clave, o especificar un valor predeterminado para la clave inexistente.</td>
        </tr>
        <tr>
            <td>IndexError</td>
            <td>Ocurre cuando se intenta acceder a un elemento de una lista con un índice fuera de rango.</td>
            <td>Verificar que el índice esté dentro del rango válido de la lista antes de acceder al elemento. Utilizar el método `len()` para obtener la longitud de la lista y el método `range()` para generar una secuencia de índices válidos.</td>
        </tr>
        <tr>
            <td>FileNotFoundError</td>
            <td>Ocurre cuando se intenta abrir un archivo que no existe.</td>
            <td>Verificar que la ruta del archivo sea válida y que el archivo exista antes de intentar abrirlo. Utilizar la función `os.path.exists()` para verificar si un archivo existe.</td>
        </tr>
        <tr>
            <td>ImportError</td>
            <td>Ocurre cuando se intenta importar un módulo que no existe o no está disponible.</td>
            <td>Verificar que el módulo esté instalado correctamente y que la ruta de importación sea válida. Utilizar la función `importlib.util.find_spec()` para verificar si un módulo existe.</td>
        </tr>
        <tr>
            <td>ZeroDivisionError</td>
            <td>Ocurre cuando se intenta dividir por cero.</td>
            <td>Validar el denominador antes de realizar la operación de división. Asegurarse de que el denominador no sea cero.</td>
        </tr>
        <tr>
            <td>AttributeError</td>
            <td>Ocurre cuando se intenta acceder a un atributo de un objeto que no lo posee.</td>
            <td>Verificar si el atributo existe en el objeto antes de acceder a él. Utilizar la función `hasattr()` para verificar si un objeto tiene un atributo específico.</td>
        </tr>
    </tbody>
</table>

### Creando Excepciones propias
Para crear una excepción personalizada, definimos una nueva clase que herede de la clase `Exception` (en efecto, se tuvo que esperar 1 semestre para ver el `try`, entender el concepto de clase y poder heradar de `Exception`). 

```python
class MiExcepcion(Exception):
  """
  Excepción personalizada para un caso específico.
  """
  # Se puede poner un print con la información de la excepcion
  pass
```

Alternativamente:

```python
class MiExcepcion(Exception):
  """
  Excepción personalizada para un caso específico.

  Args:
    message: Mensaje informativo sobre la excepción.
  """

  def __init__(self, message):
    super().__init__(message)
```

**Ejemplo:** Excepciones como clases.
```python
class ValorInvalidoException(Exception):
  def __init__(self, message):
    super().__init__(message)

class Calculadora:
  def dividir(self, numerador, denominador):
    """
    Divide dos números.

    Args:
      numerador: El dividendo.
      denominador: El divisor.

    Returns:
      Resultado de la división.
    """
    if denominador == 0:
      raise ValueError("No se puede dividir por cero.")
    if not isinstance(numerador, (int, float)) or not isinstance(denominador, (int, float)):
      raise ValorInvalidoException("Los valores deben ser números.")
    return numerador / denominador

try:
  calculadora = Calculadora()
  resultado = calculadora.dividir("5", 2)
  print(f"El resultado de la división es: {resultado}")
except ValueError as error:
  print(f"Error: {error}")
except ValorInvalidoException as error:
  print(f"Error: {error}")
```

**Explicación:** En este ejemplo, la clase Calculadora define la excepción `ValorInvalidoException` para indicar cuando se introducen valores no válidos para la operación de división.


## Reto 6: 
1. Add the required exceptions in the Reto 1 code assigments.
2. In the package `Shape` identify at least cases where exceptions are needed (maybe when validate input data, or math procedures) explain them clearly using comments and add them to the code.

P.D. Happy codding!