**Projeto: BelezaFemme - Gestão de Estoque**

## 1. Tema Escolhido: 
O tema escolhido para a aplicação foi o Controle de Estoque para uma loja de roupas femininas fictícia chamada BelezaFemme.

## 2. O que o sistema faz?
O sistema permite que o administrador da loja gerencie seu estoque de forma digital. Através de um menu no terminal , é possível cadastrar novos itens, visualizar todos os produtos armazenados, pesquisar itens específicos por ID, atualizar informações de preços ou quantidades e remover produtos do sistema.

## 3. Como o CRUD foi aplicado?
**Create (Criar):**  Implementado na função criar(lista), onde um novo dicionário é gerado com os dados do produto e adicionado à lista principal. O ID é gerado automaticamente seguindo a fórmula $novo\_id = len(lista) + 1$.
**Read (Ler):** Foi  aplicado de duas formas, a primeira na função listar(lista), que exibe todos os produtos , e na função ler(lista, id), que busca e retorna os detalhes de um único registro através de seu Id.
**Update (Atualizar):**  Implementado na função atualizar(lista, id), permitindo a modificação de campos específicos de um dicionário já existente.
**(Deletar):**  Implementado na função deletar(lista, id), que remove o dicionário correspondente ao ID informado da lista de registros.

## 4. Requisitos Técnicos Utilizados:
**Listas:** Para o armazenamento dinâmico de todos os registros em memória.
**Dicionários:** Para representar cada produto de forma estruturada (ID, Nome, Categoria, Preço, Quantidade).
**JSON:** Utilizado para o armazenamento de dados através das funções carregar() e salvar(lista), garantindo que as informações não sejam perdidas ao fechar o programa.
**Tratamento de Erros:** O sistema valida se o usuário digita números válidos para IDs e preços, impede que campos obrigatórios fiquem vazios e trata tentativas de acesso a IDs inexistentes.
