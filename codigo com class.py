import os
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome = str
    idade = int
    altura = float
    peso = float
class Final:
    lista_final:list


def menu():
    print("""
Código  |   Descrição
   1    |  Adicionar pessoa
   2    |  Exibir resultados
   3    |  Sair
""")
def limpar_tela():
    os.system("cls || clear ")

def criando_arquivo(a, b):
    with open(a,"a") as arquivo_Pessoa:
        for Pessoa in b:
            arquivo_Pessoa.write(f"{Pessoa.nome},{Pessoa.idade},{Pessoa.altura},{Pessoa.peso}\n")
        arquivo_Pessoa.close()

def criando_arquivo_final(a, b):
    with open(a,"a") as arquivo_Pessoa:
        for Pessoa in b:
            arquivo_Pessoa.write(f"{Pessoa}, \n")
        arquivo_Pessoa.close()

def lendo_arquivos(a):
    lista_final = []
    with open(a, "r") as lendo_Pessoa:
        for linha in lendo_Pessoa:
            nome,idade, altura, peso = linha.strip().split(",")
            lista_final.append(Pessoa(nome = int(nome),idade = int(idade), altura = altura, peso = float(peso)))
        lendo_Pessoa.close()
    return lista_final

def logoSenai():
    print("="*40)
    print(f"{"Senai":^40}")
    print("="*40)


def imc(a:float,b:float):
    lista_imc = []
    for i,peso in enumerate(b):
        imc = peso/(a[i]*a[i])
        lista_imc.append(imc)
    return lista_imc

def classificacao_imc(resposta):
    if resposta >= 40:
        return 'Obesidade grau 3'
    elif resposta >= 35:
        return'Obesidade grau 2'
    elif resposta >= 30:
            return'Obesidade grau 1'
    elif resposta >= 25:
        return'Sobrepeso'
    elif resposta >=18.5:
        return 'Peso normal'
    elif resposta <= 18.5:
        return'Abaixo do peso'
lista_Pessoa = []
while True:
    menu()
    opcao = input("Resposta: ")
    match opcao:
        case "1":
            pessoa = Pessoa(
                nome = input("Digite seu nome: "),
                idade = int(input("Digite sua idade: ")),
                altura = float(input("Digite sua altura: ")),
                peso = float(input("Digite seu peso: "))
            )
            lista_Pessoa.append(pessoa)
            nome_arquivo = "Aquivo Pessoa.txt"
            criando_arquivo(nome_arquivo,lista_Pessoa)
            limpar_tela()
        case "2":
            limpar_tela()
            nome_arquivo = "Dados.txt"
            lista_definitiva = lendo_arquivo(nome_arquivo)
            imc = calculando_imc(lista_definitiva)
            analise_imc = analisando_imc(imc)
            nome_arquivo1 = "pesquisa_IMC.txt"
            criando_arquivo_final(nome_arquivo1, imc)
            print("="*40)
            print(f"{"Resultado":^40}")
            print("="*40)
            for i, cliente in enumerate(lista_definitiva):
                print(f"\nNome: {cliente.nome}")
                print(f"Idade: {cliente.idade}")
                print(f"Altura: {cliente.altura}")
                print(f"Peso: {cliente.peso}")
                print(f"Seu IMC é: {imc[i]:.2f}")
                print(f"Grau: {analise_imc[i]}")

        case "3":
            break
            
        case _:
            print("Opção inválida")
            continue
                


