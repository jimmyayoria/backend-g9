# esto es un comentario

nombre="eduardo"
edad=40
apellido='Jose'

despedida="""el dia de hoy
nos despedimos, hasta una 
nueva oportunidad"""

lastName="O'neal"

print (nombre)
print (apellido)

#en python no hay ni null ni undefined ni NaN (not a number) todo ello se resume en None
#aqui estoy declarando una variable sin contenido
especialidad = None
print(especialidad)

# no hay validaciones al momento der cambiar el yipo de dato
lastName=80
lastName=None

#type(var) > devolver que tipo de dato es esa variable
print(type(nombre))
print(type(edad))

#tambien se puede declarar varias variables en una misma linea
curso, grupo, mes, dia, nota='Codigo' , 'Backend' , 'Octubre', '10', '18'
print(curso, grupo, mes)
print(grupo)

#id(var) > mostrar la posicion de memoria en el cual se esta alojando la variable
print(id(curso))

# del > elimina la variable (libera la memoria), no se puede volver a utilizar esa variable nunca mas
del curso
print(curso)
