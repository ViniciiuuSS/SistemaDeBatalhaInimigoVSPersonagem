from time import sleep
from random import randint

print("\033[7;33;40m-=-" * 54)
jo = ("\033[7;33;40m Sistema de batalha entre personagem e inimigo")
print(jo.center(170))
print("\033[7;33;40m-=-" * 54)
#----------------------------------------------------------------------------------------------------------------------


faca = 15
zumbi = 15
vida = 50
while zumbi > 0:
    ataq = int(input(f"FACA = {faca} Vida = {vida}\n[1]Atacar\n[2]Não atacar\nEscolha = "))
    if ataq == 1:
        print("ATACANDO...")
        sleep(1)
        dano = randint(1,5)
        zumbi -= dano
        desgasto = randint(1, 3)
        faca -= desgasto
        print(f"Voce o atacou a pessoa ficou com = {zumbi} de vida\n e sua faca ficou com {faca} restante")
        if zumbi == 0:
            print("Pessoa morreu!")
        elif faca == 0:
            print("FACA QUEBROU")
            while faca == 0:
                ataq = int(input("[1]Atacar\n[2]Não atacar\nEscolha = "))
                print("ATACANDO...")
                sleep(1)
                dano = randint(1, 2)
                zumbi -= dano
                print(f"Voce o atacou a pessoa ficou com = {zumbi} de vida\n")

    elif ataq == 2:
       print("Pessoa vai te atacar..")
       atapeso = randint(1,2)
       if atapeso == 1:
        sleep(1)
        dano = randint(1,5)
        vida -= dano
        print(f"Voce ficou com = {vida} de vida")
       elif atapeso == 2:
           print("Pessoa errou o ataque!")



