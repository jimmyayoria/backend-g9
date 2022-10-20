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
# print(int(eduardo)) # no se puede convertir tipos de datos irreales
print(type(numero1) == type(numero2))

# MAYOR / MAYOR O IGUAL
print(10 > 9.58)
print(10 > int('5'))
print(50 >= 30)

# MENOR / MENOR O IGUAL
print(50 < 80)
print(50 <= 50)
# siempre va el simbolo de mayor o menor antes que el igual, nunca al revez porque python entiende que se esta tratando de una asignacion
print(100<= float('40.24'))
print (100<=40.52)

# --------------------------------------------
# OPERADORES LOGICOS  --> Sirven para comparar varias condicionales
# --------------------------------------------

# && para indicar un AND , en python se usa la palabra AND
# || para indicar un OR , en python se usa la palabra OR

# and  ---> todas las condiciones deben ser verdaderas para que sea verdadero
eduardo=30
ronald=25
henry=25
carmen=19
angel=15

print((angel > eduardo) and (ronald < henry))

print((eduardo > angel) and (carmen < ronald))

# or -----> AL MENOS una condicion tiene que ser verdadera para que toda sea verdadero

print((carmen > ronald) or (eduardo > ronald))

# COMPUERTA LOGICA ( operador and)
#  V1 |  V2  |  R
#  F  |   F  |  F
#  V  |   F  |  F
#  F  |   V  |  F
#  V  |   V  |  V

# COMPUERTA LOGICA (Operador or)
#  V1 |  V2  |  R
#  F  |   F  |  F
#  V  |   F  |  V
#  F  |   V  |  V
#  V  |   V  |  V

# --------------------------------------------
# OPERADORES DE IDENTIDAD  --> Sirven para comparar varias condicionales
# ------------------------------------------

verduras = ['apio','rocoto','zanahoria']
print('rocoto' in verduras)
print('champiñon' not in verduras)
print(('apio','rocoto') in verduras)





 