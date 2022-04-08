import os
import json
produtos = list()


def menuPrincipal():
    while True:
        print("========================")
        print("   João Varejos   ")
        print("========================")
        print("[1] - CadastrarProduto")
        print("[2] - Relatorio de Produtos")
        print("[3] - Relatório de Estoque Baixo")
        print("[4] - Exportar dados")
        print("[0] - Sair")
        res = int(input("Opcao: "))
        if res == 0:
            LimparTela()
            print("Saindo da Aplicacao")
            break
        if res == 1:
            LimparTela()
            CadastrarProduto()
            while 1:
                op = input(
                    "Deseja Cadastrar outro Produto? S para sim ,qualquer tecla para Voltar ao Menu Principal\n")
                if (op == "S" or op == "s"):
                    LimparTela()
                    CadastrarProduto()
                else:
                    LimparTela()
                    menuPrincipal()
                    return False
        if res == 2:
            LimparTela()
            GerarRelatorios()
        if res == 3:
            LimparTela()
            estoqueBaixo()
        if res == 4:
            ExportarJson()


def CadastrarProduto():
    produto = dict()
    produto['nome'] = str(input('Nome do Produto:'))
    produto['valorCompra'] = float(input('\nValor de Compra do produto:'))
    produto['qtdEstoque'] = int(input("\nQuantidade em estoque:"))
    produto['valorVenda'] = produto['valorCompra'] * 1.25
    produto['codigo'] = len(produtos)+1
    produtos.append(produto)


def mostraValores(produto):
    print("Codigo: {}\nNome:{}\nValor da Compra:{}\nEstoque: {} \nValor de Venda{}".format(
        produto['codigo'], produto['nome'], produto['valorCompra'], produto['qtdEstoque'], produto['valorVenda']))


def estoqueBaixo():
    produtos.sort(key=lambda produto: produto["qtdEstoque"])
    print("Relatorio de estoque baixo")
    for p in produtos:
        if p["qtdEstoque"] <= 5:
            mostraValores(p)


def GerarRelatorios():
    produtos.sort(key=lambda produto: produto["nome"])
    print("Relatório de todos os produtos")
    for p in produtos:
        mostraValores(p)


def LimparTela():
    os.system("clear")


def ExportarJson():
    jsonString = json.dumps(produtos)
    print(jsonString)


menuPrincipal()
