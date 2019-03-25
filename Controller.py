from Armas import Armas

from os import system, name 


def cls():

    if name == 'nt':
        system('cls')

    else:
        system('clear')

    return False


def addArma():


    return False

def listArmas():


    return False

def deleteArma():


    return False

def checar():


    return False

def existCheck():


    return False


class Controller:
            

    print("Bem vindo ao programa de armas do Borderlands 2!\n")

    while(True):

        print("Digite 1 para adicionar uma arma, 2 para listar as armas, 3 para checar se uma arma está na lista, 4 para deletar uma arma, 5 para mais informações, e alguma outra coisa para sair.\n")

        choice = input("Escolha: ")

        cls()

        

        if(choice == '1'):

            print("\nAdicionando uma arma.\n")

        elif(choice == '2'):

            print("\nAs armas atuais são: \n")
                
        elif(choice == '3'):

            print("\nChecando se a arma está na lista\n")

        elif(choice == '4'):

            print("\nDeletando uma arma.\n")

        elif(choice == '5'):

            print("\nInfo\n")

        else:
            print("Deseja mesmo fechar o programa?")
                    
            exit = input("Escolha: ")

            cls()

            if(exit == 's' or exit == 'S' or exit == 'Sim' or exit == 'sim'):

                print("Obrigado por usar o programa!\n")
                input()
                break

   ## TESTE :::: arma = Armas("Grog Nozzle", "Maliwan",55555,55555,55555,2.1,20,25,"Azul","Pode deixar bêbado, cura, Sempre dá slag, arma de missão")

        
