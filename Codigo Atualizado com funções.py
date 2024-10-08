import os
os.system("cls || clear")

def logoSenai():
    os.system("cls || clear")
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
     

nomes = []
idades = []
alturas = []
pesos = []

while True:
    
    nome = input("Digite o nome e sobrenome do usuario ou digite sair pare encerrar: ")
    if nome.lower() == 'sair':
        break

    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    

calculo_imc = imc(alturas, pesos)
classificacoes = [classificacao_imc(imc_valor) for imc_valor in calculo_imc]

logoSenai()
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}")
    print(f"Idade: {idades[i]}")
    print(f"Calculo do IMC: {calculo_imc[i]:.2f}")
    print(f"Classificação: {classificacoes[i]}")




