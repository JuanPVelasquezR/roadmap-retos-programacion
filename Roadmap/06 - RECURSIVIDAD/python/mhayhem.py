# Entiende el concepto de recursividad creando una función recursiva que imprima
# números del 100 al 0.

def countdown(n):
    if n < 0:
        pass
    else:
        print(n)
        countdown(n - 1)
countdown(100)

# DIFICULTAD EXTRA (opcional):
# Utiliza el concepto de recursividad para:
# - Calcular el factorial de un número concreto (la función recibe ese número).
# - Calcular el valor de un elemento concreto (según su posición) en la 
#   sucesión de Fibonacci (la función recibe la posición).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
        
print(factorial(9))

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(25))