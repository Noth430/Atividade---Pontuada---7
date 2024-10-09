import os
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    idade:int
    altura:float
    peso:float
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

def lendo_arquivos(nome_arquivo):
    lista_final = []
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            nome, idade, altura, peso = linha.strip().split(",")
            assert len(nome) > 0, "Nome não pode ser vazio"
            lista_final.append(Pessoa(nome=nome, idade=int(idade), altura=float(altura), peso=float(peso)))
    return lista_final

def logoSenai():
    print("="*40)
    print(f"{"Senai":^40}")
    print("="*40)


def imc(a):
    lista_imc = []
    for cliente in a:
        imc = cliente.peso/(cliente.altura**2)
        lista_imc.append(imc)
    return lista_imc

def analisando_imc(a:float):
    lista_analise_imc = []

    for cliente in a:
        if cliente >= 40:
            lista_analise_imc.append("Obesidade grau 3")
        elif cliente >= 35:
            lista_analise_imc.append("Obesidade grau 2")
        elif cliente >= 30:
            lista_analise_imc.append("Obesidade grau 1")
        elif cliente >= 25:
            lista_analise_imc.append("Sobrepeso")
        elif cliente >=18.5:
            lista_analise_imc.append("Peso normal")
        elif cliente <= 18.5:
            lista_analise_imc.append("Abaixo do peso")

    return lista_analise_imc
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
            nome_arquivo = "Aquivo Pessoa.txt"
            lista_definitiva = lendo_arquivos(nome_arquivo)
            imcs = imc(lista_definitiva)
            analizando_imc = analisando_imc(imcs)
            nome_arquivo1 = "pesquisa_IMC.txt"
            criando_arquivo_final(nome_arquivo1, imcs)
            print("="*40)
            print(f"{"Resultado":^40}")
            print("="*40)
            for i, cliente in enumerate(lista_definitiva):
                print(f"\nNome: {cliente.nome}")
                print(f"Idade: {cliente.idade}")
                print(f"Altura: {cliente.altura}")
                print(f"Peso: {cliente.peso}")
                print(f"Seu IMC é: {imcs[i]:.2f}")
                print(f"Grau: {analizando_imc[i]}")

        case "3":
            break
            
        case _:
            print("Opção inválida")
            continue
                


