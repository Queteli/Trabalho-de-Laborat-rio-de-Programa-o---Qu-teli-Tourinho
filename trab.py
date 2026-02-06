import json
import os

ARQUIVO_JSON = "estoque.json"
lista_produtos = []

def carregar():
    global lista_produtos
    if os.path.exists(ARQUIVO_JSON):
        try:
            with open(ARQUIVO_JSON, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                lista_produtos = json.loads(conteudo) if conteudo else []
        except (json.JSONDecodeError, Exception):
            lista_produtos = []
    else:
        lista_produtos = []


def salvar(lista):
    with open(ARQUIVO_JSON, 'w', encoding='utf-8') as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)


def listar(lista):
    print("\n" + " LISTAGEM DE PRODUTOS ".center(50, "-"))
    if not lista:
        print("Nenhum registro encontrado.")
    else:
        for p in lista:
            print(f"ID: {p['id']} | Nome: {p['Nome']} | Qtd: {p['Quantidade']}")
    print("-" * 50)
    input("\nPressione Enter para voltar ao menu...")


def criar(lista):
    print("\n" + " NOVO PRODUTO ".center(50, "-"))
    # Requisito 3.4: ID Automático len(lista)+1 
    novo_id = len(lista) + 1
    
    nome = input("Nome do produto: ").strip()
    categoria = input("Categoria: ").strip()
    
 
    if not nome or not categoria:
        print("Erro: Campos obrigatórios não podem ficar vazios!")
        return
        
    try:
        preco = float(input("Preço: "))
        qtd = int(input("Quantidade: "))
        
    
        produto = {
            'id': novo_id,
            'Nome': nome,
            'Categoria': categoria,
            'Preço': preco,
            'Quantidade': qtd
        }
        
        lista.append(produto)
        salvar(lista)
        print("Cadastrado com sucesso!")
    except ValueError:
        print("Erro: Digite valores numéricos válidos para preço e quantidade.")


def ler(lista, id_busca):
    for p in lista:
        if p['id'] == id_busca:
            return p
    return None


def atualizar(lista, id_busca):
    produto = ler(lista, id_busca)
    if produto:
        print(f"Editando: {produto['Nome']}")
        produto['Nome'] = input(f"Novo nome ({produto['Nome']}): ") or produto['Nome']
        try:
            p_input = input(f"Novo preço ({produto['Preço']}): ")
            if p_input: produto['Preço'] = float(p_input)
            
            q_input = input(f"Nova quantidade ({produto['Quantidade']}): ")
            if q_input: produto['Quantidade'] = int(q_input)
            
            salvar(lista)
            print("Atualizado com sucesso!")
        except ValueError:
            print("Erro: Valor inválido. Alterações numéricas descartadas.")
    else:
        print("Erro: ID não encontrado.")


def deletar(lista, id_busca):
    global lista_produtos
    produto = ler(lista, id_busca)
    if produto:
        confirmar = input(f"Excluir {produto['Nome']}? (s/n): ").lower()
        if confirmar == 's':
            lista_produtos = [p for p in lista if p['id'] != id_busca]
            salvar(lista_produtos)
            print("Excluído!")
    else:
        print("Erro: ID não encontrado.")


def menu():
    while True:
        print("\n" + " BELEZA FEMME - GESTÃO ".center(50, "="))
        print("1 - Listar Todos")
        print("2 - Criar Novo")
        print("3 - Ler/Pesquisar por ID")
        print("4 - Atualizar")
        print("5 - Deletar")
        print("0 - Sair")
        
        op = input("\nEscolha uma opção: ")
        
        if op == '1':
            listar(lista_produtos)
        elif op == '2':
            criar(lista_produtos)
        elif op == '3':
            try:
                id_digitado = int(input("Digite o ID: "))
                res = ler(lista_produtos, id_digitado)
                if res:
                    print(f"\nENCONTRADO: {res}")
                else:
                    print("ID não existe.")
            except ValueError:
                print("Erro: Digite um número de ID válido.")
        elif op == '4':
            try:
                id_digitado = int(input("ID para atualizar: "))
                atualizar(lista_produtos, id_digitado)
            except ValueError:
                print("ID inválido.")
        elif op == '5':
            try:
                id_digitado = int(input("ID para deletar: "))
                deletar(lista_produtos, id_digitado)
            except ValueError:
                print("ID inválido.")
        elif op == '0':
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    carregar()

    menu()
