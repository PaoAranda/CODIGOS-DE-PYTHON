#encoding:UTF-8
import random

aleatorio = random.randrange(0, 5)
eligePc = ""
print("1)Piedra")
print("2)Papel")
print("3)Tijera")
print("4)Lagarto")
print("5)Spock5")

opcion = int(input("\nQue eliges: "))

if opcion == 0:
    eligeUsuario = "piedra"
elif opcion == 1:
    eligeUsuario = "papel"
elif opcion == 2:
    eligeUsuario = "tijera"
elif opcion == 3:
    eligeUsuario = "Lagarto"
elif opcion == 4:
    eligeUsuario = "Spock"

print("Tu eliges: ", eligeUsuario)

if aleatorio == 1:
    eligePc = "piedra"
elif aleatorio == 2:
    eligePc = "papel"
elif aleatorio == 3:
    eligePc = "tijera"
elif aleatorio == 4:
    eligePc = "Lagarto"
elif aleatorio == 5:
    eligePc = "Spock"

print("PC eligió: ", eligePc)
print("...")

if eligePc == "tijeras" and eligeUsuario == "Papel":
    print("Ganaste, tijeras cortan papel")
elif eligePc == "papel" and eligeUsuario == "piedra":
    print("Ganaste, papel tapa piedra")
elif eligePc == "piedra" and eligeUsuario == "Lagarto":
    print("Ganaste, Piedra aplasta a Lagarto")
elif eligePc == "Lagarto" and eligeUsuario == "Spock":
    print("Ganaste, Lagarto envenena a Spock")
if eligePc == "tijeras" and eligeUsuario == "lagarto":
    print("Perdiste, tijeras decapita lagarto")
if eligePc == "lagarto" and eligeUsuario == "papel":
    print("Perdiste, Lagarto devora papel")
elif eligePc == "papel" and eligeUsuario == "spock":
    print("Perdiste, Papel desautoriza pock")
elif eligePc == "spock" and eligeUsuario == "piedra":
    print("Perdiste, Spock vaporiza Piedra")
elif eligePc == "piedra" and eligeUsuario == "tijeras":
    print("Perdiste, piedra aplasta tijeras")

if eligePc == eligeUsuario:
    print("empate")
    


