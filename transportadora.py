import os
from funcoesTransportadora import *

def main():
    iniciar_programa()
    produtos = []
    while True:
        os.system("clear")
        opcao = exibir_menu()
        if opcao == 1:
            os.system("clear")
            produtos = cadastra_produtos(produtos)
        elif opcao == 2:
            os.system("clear")
            exibir_produtos_cadastrados(produtos)
            input("Pressione qualquer tecla para retornar ao menu... ")
        elif opcao == 3:
            capacidade = coleta_capacidade_do_caminhao()
            tabelaKnapsack, itensLevados = executa_knapsack(produtos, capacidade)
            print("================ TABELA KNAPSACK ITERATIVA ========================")
            print(" | ", end="")
            for i in range(0, capacidade+1):
                print(i, end="\t")
            print()
            i = 0
            for linha in tabelaKnapsack:
                print(i, end="| ")
                for coluna in linha:
                    print(coluna, end="\t")
                print()
                i += 1
            print("\n\n\033[0;32mLista de itens levados: \033[0m") 
            for i in range(0, len(itensLevados)):
                print("Nome do produto: ", itensLevados[i][0])
                print("Quantidade: ", itensLevados[i][1])
                print("Valor(R$): ", itensLevados[i][2])
                print("Peso(g): ", itensLevados[i][3])
                print("-------------------")
            input("Pressione qualquer tecla para retornar ao menu... ")
        else:
            os.system("clear")
            print("Programa encerrado com sucesso!")
            break

main()