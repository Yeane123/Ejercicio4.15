#dibujar un cuadrado
print("Ingrese el número para el tamaño del lado:")
lado1=int(input("Ingrese el tamaño de columnas:"))
lado2=int(input("Ingrese el tamaño de filas:"))

for i in range(1,lado2+1):
    for j in range(1, lado1+1):
        print("*", end="")

    print("")

input()