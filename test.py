def dividir(numerador, denominador):
  return numerador / denominador

try:
  resultado = dividir(10, 0)
  print(f"El resultado de la división es: {resultado}")
except Exception as e:
  print(f"Error: {e}")