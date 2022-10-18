# -------------------------------------
#       OPERADORES ARITMETICOS
# -------------------------------------

numero1, numero2 =10, 50

# SUMA
# Nota: solamente sera suma si las 2 variables son nunmericos, si son string entonces se hara concatenacion y adrmas no se puede sumar entre string y numeros
print(numero1 + numero2)

# RESTA
# solo para numeros
print(numero1 - numero2)

# MULTIPLICACION
# nota: si se usa la multuiplicacon en un string, entonces este se repetira el numero de veces entre un string y un numero de veces
print(numero1*numero2)
print('Hola '*5)

# DIVISION
print(numero1/numero2)

# MODULO
print(numero1 % numero2)

# COCIENTE
print(numero1 // numero2)

# EXPONENTE
print(numero1 ** numero2)

# RAIZ CUADRADA usando exponente
print(numero1 ** 0.5)

# -----------------------------------------
#         OPERADORES DE ASIGNACION
# -----------------------------------------

# IGUAL  asignar un nuevo valor a una variable
numero1 = 100

# INCREMENTO
numero1 += 1 # _incrementando el valor del numero1 en una unidad
print(numero1)

# DECREMENTO
numero1 -= 1 
print(numero1)

# MULTIPLICADOR
numero1 *= 2
print(numero1)

# DIVIDENDO
numero1 /= 5 # numero1 = numero1 / 5

# -----------------------------------------
#        OPERADORES DE COMPARACION  ---> siempre retornaran un booleano (si es verdadero o si es falso)
# -----------------------------------------

# IGUAL QUE
# en Python a diferencia de JS no existe el triple Igual
print(numero1) # float
print(numero2) # Int
print(numero1 == numero2)
print(int(40.7)) # le quita el decimal
print(type(numero1) == type(numero2))




 