# --- Criar a lista de compras --- #
lista_compras = ['banana', 'maçã', 'carne', 'azeite', 'sal', 'arroz']

# --- Criar a lista que será do carrinho --- #
carrinho = []

# --- A compra está em andamento --- #
comprando = True

# --- Repetir a ação de colocar os produtos no carrinho até que a lista esteja vazia --- #
while comprando:
    # --- Retirar o produto da lista --- #
    produto = lista_compras.pop()

    # --- Colocar o produto no carrinho --- #
    carrinho.append(produto)

    # --- Verificar se todos os produtos da lista foram colocados no carrinho --- #
    if not lista_compras:
        # --- Parar de comprar --- #
        comprando = False

# --- Nome do mercado --- #
NOME_MERCADO = 'Mercado do Zé'

# --- Pagar os produtos --- #
print(f'Pagar ao mercado: {NOME_MERCADO}')
for produto in carrinho:
    print(f'Pagar produto: {produto}')
