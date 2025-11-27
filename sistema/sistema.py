import flet as ft

# Função de callback para adicionar um produto ao carrinho
def adicionar_ao_carrinho(e, page, produto_nome, preco, quantidade):
    carrinho = page.controls[3]  # referenciar o carrinho
    carrinho.controls.append(ft.Text(f"Produto: {produto_nome} - Preço: R${preco} - Quantidade: {quantidade}", color="blue"))
    page.update()

# Função para cadastrar um novo produto no estoque
def cadastrar_produto(e, page, nome, preco, estoque):
    produto = f"Produto: {nome}, Preço: R${preco}, Estoque: {estoque} unidades"
    page.controls[1].controls.append(ft.Text(produto, color="green"))  # Exibe no estoque
    page.update()

# Função para finalizar a venda
def finalizar_venda(e, page):
    total = sum([float(item.text.split('R$')[1].split(' -')[0]) for item in page.controls[3].controls])  # Cálculo total da venda
    page.controls[5].controls.append(ft.Text(f"Total da Venda: R${total:.2f}", color="red"))  # Exibe o total
    page.update()

# Definindo a interface diretamente com o Flet sem a função 'main(page: ft.Page)'
page = ft.Page()
page.title = "PDV - Sistema de Ponto de Venda"
page.vertical_alignment = ft.MainAxisAlignment.START

# Aba de Frente de Caixa
aba_frente_de_caixa = ft.Column(
    [
        ft.Text("Frente de Caixa", size=24),
        ft.TextField(label="Produto (Código de Barras)", autofocus=True),
        ft.TextField(label="Quantidade", keyboard_type=ft.KeyboardType.NUMBER),
        ft.ElevatedButton("Adicionar ao Carrinho", on_click=lambda e: adicionar_ao_carrinho(e, page, "Produto A", 10.99, 1)),
        ft.ElevatedButton("Finalizar Venda", on_click=lambda e: finalizar_venda(e, page)),
        ft.Column([])  # Exibe o total da venda
    ]
)

# Aba de Estoque
aba_estoque = ft.Column(
    [
        ft.Text("Estoque", size=24),
        ft.TextField(label="Nome do Produto"),
        ft.TextField(label="Preço", keyboard_type=ft.KeyboardType.NUMBER),
        ft.TextField(label="Quantidade em Estoque", keyboard_type=ft.KeyboardType.NUMBER),
        ft.ElevatedButton("Cadastrar Produto", on_click=lambda e: cadastrar_produto(e, page, "Produto A", 10.99, 100)),
        ft.Column([])  # Lista de produtos cadastrados
    ]
)

# Aba de Nota Fiscal
aba_nota_fiscal = ft.Column(
    [
        ft.Text("Nota Fiscal", size=24),
        ft.Text("Nota fiscal será gerada aqui..."),
    ]
)

# Definindo as abas
abas = ft.Tabs(
    [
        ft.Tab("Frente de Caixa", aba_frente_de_caixa),
        ft.Tab("Estoque", aba_estoque),
        ft.Tab("Nota Fiscal", aba_nota_fiscal),
    ]
)

# Adicionando as abas na página
page.add(abas)

# Inicializa a aplicação diretamente
ft.app(target=lambda: page)
