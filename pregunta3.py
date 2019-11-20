

nombre = input("¿Cual es su nombre?: ")
sexo = input("¿Que sexo es ?")
edad = int(input("¿Cuantos años tiene?: ")) 
while sexo=="femenino" or sexo=="masculino":
    print("Error,por favor escriba de nuevo")
    sexo = input("¿Que sexo es :?")

while edad<=5 and edad>=17:
    print("Error,por favor escriba de nuevo")
    edad = int(input("¿Cuantos años tiene?: "))    


print("------Lista de inscritos------")
print(nombre)
print(sexo)
print(edad)        