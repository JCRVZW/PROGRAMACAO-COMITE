import flet as ft

# Produtos iniciais
produtos = {
    "789100000001": {"nome": "Arroz 5kg", "preco": 21.50, "estoque": 30, "desconto": 0.0},
    "789100000002": {"nome": "Feijão 1kg", "preco": 7.80, "estoque": 50, "desconto": 0.10},
    "789100000003": {"nome": "Açúcar 5kg", "preco": 12.40, "estoque": 12, "desconto": 0.05},
}

def main(page: ft.Page):
    page.title = "PDV — Mercado Colorido"
    page.window_width = 1280
    page.window_height = 720
    page.padding = 0
    page.bgcolor = ft.Colors.BLACK

    carrinho = []
    total_value = 0.0
    caixa_aberto = False
    valor_caixa = 0.0

    # --- Funções de estilo ---
    def painel_titulo(texto, cor="#FF00FF"):
        return ft.Container(
            alignment=ft.alignment.center,
            bgcolor=cor,
            padding=10,
            border_radius=10,
            content=ft.Text(texto, size=22, color="white", weight="bold"),
        )

    def campo_label(texto, cor="white"):
        return ft.Text(texto, size=15, weight="bold", color=cor)

    # --- Atualizar tabela PDV ---
    tabela_pdv = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Item", weight="bold")),
            ft.DataColumn(ft.Text("Código", weight="bold")),
            ft.DataColumn(ft.Text("Descrição", weight="bold")),
            ft.DataColumn(ft.Text("Qtd", weight="bold")),
            ft.DataColumn(ft.Text("Vlr Unit.", weight="bold")),
            ft.DataColumn(ft.Text("Total", weight="bold")),
        ],
        rows=[],
        border=ft.border.all(1, "gray"),
        column_spacing=10,
        vertical_lines=True,
        horizontal_lines=True,
    )

    aviso_produto = ft.Text("", size=16, color="red")

    def atualizar_tabela():
        nonlocal total_value
        tabela_pdv.rows.clear()
        total_value = 0
        for i, item in enumerate(carrinho, start=1):
            subtotal = item["preco"] * item["qtd"]
            total_value += subtotal
            tabela_pdv.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(i))),
                        ft.DataCell(ft.Text(item["codigo"])),
                        ft.DataCell(ft.Text(item["nome"])),
                        ft.DataCell(ft.Text(str(item["qtd"]))),
                        ft.DataCell(ft.Text(f"R$ {item['preco']:.2f}")),
                        ft.DataCell(ft.Text(f"R$ {subtotal:.2f}")),
                    ]
                )
            )
        subtotal_text.value = f"R$ {total_value:.2f}"
        page.update()

    # --- Adicionar produto ---
    def adicionar_produto(cod):
        if cod in produtos and produtos[cod]["estoque"] > 0:
            aviso_produto.value = ""
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
            atualizar_estoque()
        else:
            aviso_produto.value = "Produto não encontrado ou sem estoque!"
            valor_unitario.value = "R$ 0,00"
            total_item.value = "R$ 0,00"
            page.update()

    # --- Campos PDV ---
    def on_submit(e):
        codigo = campo_codigo.value.strip()
        campo_codigo.value = ""
        adicionar_produto(codigo)

    campo_codigo = ft.TextField(bgcolor="#FF33AA", border_radius=10, hint_text="Digite ou escaneie o código", on_submit=on_submit)
    valor_unitario = ft.Text("R$ 0,00", size=20, weight="bold", color="#00FFDD")
    total_item = ft.Text("R$ 0,00", size=20, weight="bold", color="#00FFDD")
    campo_recebido = ft.TextField(bgcolor="#FF33AA", border_radius=10, hint_text="Valor recebido")

    def calcular_troco(e):
        try:
            recebido = float(campo_recebido.value.replace(",", "."))
            troco = recebido - total_value
            troco_text.value = f"R$ {troco:.2f}"
            page.update()
        except:
            aviso_produto.value = "Valor recebido inválido!"
            page.update()

    subtotal_text = ft.Text("R$ 0,00", size=30, weight="bold", color="#FFFF00")
    troco_text = ft.Text("R$ 0,00", size=30, weight="bold", color="#FFFF00")

    # --- Painéis ---
    painel_esquerdo = ft.Container(
        width=350,
        padding=20,
        bgcolor="#551A8B",
        border_radius=15,
        content=ft.Column([
            painel_titulo("CÓDIGO DE BARRAS", "#FF007F"),
            campo_codigo,
            aviso_produto,
            ft.Divider(height=20, color="transparent"),
            painel_titulo("VALOR UNITÁRIO", "#FF4500"),
            valor_unitario,
            ft.Divider(height=20, color="transparent"),
            painel_titulo("TOTAL DO ITEM", "#00CED1"),
            total_item,
            ft.Container(expand=True),
        ]),
    )

    painel_central = ft.Container(
        expand=True,
        padding=10,
        content=ft.Column([
            painel_titulo("LISTA DE PRODUTOS", "#7FFF00"),
            ft.Container(
                bgcolor="#222222",
                padding=10,
                border_radius=15,
                content=ft.Column([tabela_pdv], scroll="auto", expand=True),
                expand=True,
            ),
        ]),
    )

    painel_inferior = ft.Container(
        height=180,
        bgcolor="#551A8B",
        padding=20,
        border_radius=15,
        content=ft.Row(
            alignment="spaceBetween",
            controls=[
                ft.Column([campo_label("SUBTOTAL"), subtotal_text]),
                ft.Column([campo_label("TOTAL RECEBIDO"), campo_recebido,
                           ft.ElevatedButton("Calcular Troco", on_click=calcular_troco, bgcolor="#FF33AA")]),
                ft.Column([campo_label("TROCO"), troco_text]),
            ],
        ),
    )

    aba_pdv = ft.Column([ft.Row([painel_esquerdo, painel_central], expand=True), painel_inferior], expand=True)

    # --- Aba Estoque ---
    estoque_tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Código", weight="bold")),
            ft.DataColumn(ft.Text("Descrição", weight="bold")),
            ft.DataColumn(ft.Text("Estoque", weight="bold")),
            ft.DataColumn(ft.Text("Preço", weight="bold")),
        ],
        rows=[],
        vertical_lines=True,
        horizontal_lines=True,
        border=ft.border.all(1, "gray"),
    )

    def atualizar_estoque():
        estoque_tabela.rows.clear()
        for cod, p in produtos.items():
            estoque_tabela.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(cod)),
                    ft.DataCell(ft.Text(p["nome"])),
                    ft.DataCell(ft.Text(str(p["estoque"]))),
                    ft.DataCell(ft.Text(f"R$ {p['preco']:.2f}")),
                ])
            )
        page.update()

    atualizar_estoque()

    aba_estoque = ft.Column([
        painel_titulo("ESTOQUE DISPONÍVEL", "#00FF7F"),
        ft.Container(
            bgcolor="#222222",
            padding=10,
            border_radius=15,
            content=ft.Column([estoque_tabela], scroll="auto", expand=True),
            expand=True,
        ),
    ], expand=True)

    # --- Aba Produtos ---
    campo_cod_prod = ft.TextField(label="Código", width=300)
    campo_nome_prod = ft.TextField(label="Nome", width=300)
    campo_preco_prod = ft.TextField(label="Preço", width=300)
    campo_estoque_prod = ft.TextField(label="Estoque", width=300)

    def adicionar_produto_novo(e):
        cod = campo_cod_prod.value.strip()
        nome = campo_nome_prod.value.strip()
        try:
            preco = float(campo_preco_prod.value.replace(",", "."))
            estoque_qtd = int(campo_estoque_prod.value)
        except:
            aviso_produto.value = "Valores inválidos!"
            page.update()
            return
        produtos[cod] = {"nome": nome, "preco": preco, "estoque": estoque_qtd, "desconto": 0.0}
        atualizar_estoque()
        campo_cod_prod.value = ""
        campo_nome_prod.value = ""
        campo_preco_prod.value = ""
        campo_estoque_prod.value = ""
        page.update()

    btn_add_produto = ft.ElevatedButton("Adicionar Produto", on_click=adicionar_produto_novo, bgcolor="#FF33AA")

    aba_produtos = ft.Column([
        painel_titulo("PRODUTOS", "#FF1493"),
        ft.Column([campo_cod_prod, campo_nome_prod, campo_preco_prod, campo_estoque_prod, btn_add_produto]),
        ft.Divider(height=20),
        ft.Text("Produtos existentes:", size=18, weight="bold", color="white"),
        ft.Container(
            bgcolor="#222222",
            padding=10,
            border_radius=15,
            content=ft.Column([estoque_tabela], scroll="auto", expand=True),
            expand=True,
        ),
    ], expand=True)

    # --- Aba Caixa ---
    campo_caixa_inicial = ft.TextField(label="Valor Inicial do Caixa", width=300)
    campo_caixa_final = ft.TextField(label="Valor Final", width=300, disabled=True)
    resumo_caixa = ft.Text("", size=16, color="white")

    def abrir_caixa(e):
        nonlocal caixa_aberto, valor_caixa
        try:
            valor_caixa = float(campo_caixa_inicial.value.replace(",", "."))
            caixa_aberto = True
            resumo_caixa.value = f"Caixa aberto com R$ {valor_caixa:.2f}"
            campo_caixa_inicial.disabled = True
            campo_caixa_final.disabled = False
            page.update()
        except:
            aviso_produto.value = "Valor inicial inválido!"
            page.update()

    def fechar_caixa(e):
        nonlocal caixa_aberto
        caixa_aberto = False
        campo_caixa_inicial.disabled = False
        campo_caixa_final.value = f"{valor_caixa + total_value:.2f}"
        resumo_caixa.value = f"Caixa fechado. Total vendas: R$ {total_value:.2f}"
        carrinho.clear()
        atualizar_tabela()
        atualizar_estoque()
        page.update()

    btn_abrir = ft.ElevatedButton("Abrir Caixa", on_click=abrir_caixa, bgcolor="#FF33AA")
    btn_fechar = ft.ElevatedButton("Fechar Caixa", on_click=fechar_caixa, bgcolor="#FF33AA")

    aba_caixa = ft.Column([
        painel_titulo("CAIXA", "#FF69B4"),
        campo_caixa_inicial,
        btn_abrir,
        campo_caixa_final,
        btn_fechar,
        resumo_caixa,
    ], expand=True)

    # --- TABS ---
    abas = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Frente de Caixa", content=aba_pdv),
            ft.Tab(text="Estoque", content=aba_estoque),
            ft.Tab(text="Produtos", content=aba_produtos),
            ft.Tab(text="Caixa", content=aba_caixa),
        ],
        indicator_color="#FF00FF",
        label_color="#FF00FF",
        unselected_label_color="white",
    )

    page.add(abas)
    page.update()

ft.app(target=main)
