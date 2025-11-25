import flet as ft

# Produtos exemplo
produtos = {
    "789100000001": {"nome": "Arroz 5kg", "preco": 21.50, "estoque": 30, "desconto": 0.0},
    "789100000002": {"nome": "Feijão 1kg", "preco": 7.80, "estoque": 50, "desconto": 0.10},
    "789100000003": {"nome": "Açúcar 5kg", "preco": 12.40, "estoque": 12, "desconto": 0.05},
}


def main(page: ft.Page):
    page.title = "PDV — Mercado"
    page.theme_mode = "light"
    page.window_width = 1280
    page.window_height = 720
    page.padding = 0
    page.bgcolor = "#1E3958"  # azul de fundo igual ao exemplo

    carrinho = []
    total_value = 0.0

    # Estilos reutilizáveis
    def painel_titulo(texto):
        return ft.Container(
            alignment=ft.alignment.center,
            bgcolor="#224A72",
            padding=10,
            border_radius=0,
            content=ft.Text(texto, size=22, color="white", weight="bold"),
        )

    def campo_label(texto):
        return ft.Text(texto, size=15, weight="bold", color="white")

    # Tabela de produtos
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Item", weight="bold")),
            ft.DataColumn(ft.Text("Código", weight="bold")),
            ft.DataColumn(ft.Text("Descrição", weight="bold")),
            ft.DataColumn(ft.Text("Qtd", weight="bold")),
            ft.DataColumn(ft.Text("Vlr Unit.", weight="bold")),
            ft.DataColumn(ft.Text("Total", weight="bold")),
        ],
        rows=[],
    )

    # Atualizar carrinho e tabela
    def atualizar_tabela():
        nonlocal total_value
        tabela.rows.clear()
        total_value = 0

        for i, item in enumerate(carrinho, start=1):
            subtotal = item["preco"] * item["qtd"]
            total_value += subtotal

            tabela.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(i))),
                        ft.DataCell(ft.Text(item["codigo"])),
                        ft.DataCell(ft.Text(item["nome"])),
                        ft.DataCell(ft.Text(str(item["qtd"]))),
                        ft.DataCell(ft.Text(f"{item['preco']:.2f}")),
                        ft.DataCell(ft.Text(f"{subtotal:.2f}")),
                    ]
                )
            )

        subtotal_text.value = f"R$ {total_value:.2f}"
        page.update()

    # Adicionar produto pelo código
    def adicionar_produto(cod):
        if cod in produtos:
            p = produtos[cod]
            preco_final = p["preco"] * (1 - p["desconto"])

            carrinho.append({
                "codigo": cod,
                "nome": p["nome"],
                "preco": preco_final,
                "qtd": 1
            })

            p["estoque"] -= 1
            valor_unitario.value = f"R$ {preco_final:.2f}"
            total_item.value = f"R$ {preco_final:.2f}"

            atualizar_tabela()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Produto não encontrado"), open=True)

    # Campo de código de barras
    def on_submit(e):
        codigo = campo_codigo.value.strip()
        campo_codigo.value = ""
        adicionar_produto(codigo)

    campo_codigo = ft.TextField(
        bgcolor="white",
        border_radius=5,
        on_submit=on_submit,
    )

    valor_unitario = ft.Text("R$ 0,00", size=20, weight="bold", color="white")
    total_item = ft.Text("R$ 0,00", size=20, weight="bold", color="white")

    # Troco
    campo_recebido = ft.TextField(
        bgcolor="white",
        border_radius=5,
    )

    def calcular_troco(e):
        try:
            recebido = float(campo_recebido.value.replace(",", "."))
            troco = recebido - total_value
            troco_text.value = f"R$ {troco:.2f}"
            page.update()
        except:
            page.snack_bar = ft.SnackBar(ft.Text("Valor inválido"), open=True)

    subtotal_text = ft.Text("R$ 0,00", size=30, weight="bold", color="white")
    troco_text = ft.Text("R$ 0,00", size=30, weight="bold", color="white")

    # Layout do painel lateral esquerdo
    painel_esquerdo = ft.Container(
        width=350,
        padding=20,
        bgcolor="#2F547E",
        content=ft.Column(
            controls=[
                painel_titulo("CÓDIGO DE BARRAS"),
                campo_codigo,
                ft.Divider(height=20, color="transparent"),

                painel_titulo("VALOR UNITÁRIO"),
                valor_unitario,
                ft.Divider(height=20, color="transparent"),

                painel_titulo("TOTAL DO ITEM"),
                total_item,

                ft.Container(
                    expand=True
                ),
            ],
        ),
    )

    # Painel central (tabela)
    painel_central = ft.Container(
        expand=True,
        padding=10,
        content=ft.Column(
            controls=[
                painel_titulo("LISTA DE PRODUTOS"),
                ft.Container(
                    bgcolor="white",
                    padding=10,
                    border_radius=5,
                    content=ft.Column([tabela], scroll="auto", expand=True),
                    expand=True,
                )
            ],
        ),
    )

    # Painel inferior
    painel_inferior = ft.Container(
        height=180,
        bgcolor="#2F547E",
        padding=20,
        content=ft.Row(
            alignment="spaceBetween",
            controls=[
                ft.Column(
                    controls=[
                        campo_label("SUBTOTAL"),
                        subtotal_text,
                    ]
                ),
                ft.Column(
                    controls=[
                        campo_label("TOTAL RECEBIDO"),
                        campo_recebido,
                        ft.ElevatedButton("Calcular Troco", on_click=calcular_troco),
                    ]
                ),
                ft.Column(
                    controls=[
                        campo_label("TROCO"),
                        troco_text,
                    ]
                ),
            ]
        ),
    )

    # Layout principal
    page.add(
        ft.Row(
            controls=[
                painel_esquerdo,
                painel_central
            ],
            expand=True
        ),
        painel_inferior,
    )


ft.app(target=main)
