# fundamentos-ti/tres_camadas.py
# Simula a arquitetura em 3 camadas de uma livraria online.
# Regra de ouro: cada camada só conversa com a camada vizinha.

# ---------- CAMADA 3: DADOS (faz o papel do MySQL) ----------
banco = {
    "L01": {"titulo": "Dom Casmurro", "preco": 29.90, "estoque": 3},
    "L02": {"titulo": "O Cortiço", "preco": 24.50, "estoque": 0},
}

def buscar_livro(codigo):
    """Só lê e grava. Não conhece nenhuma regra da loja."""
    return banco.get(codigo)

def baixar_estoque(codigo, qtd):
    banco[codigo]["estoque"] -= qtd

# ---------- CAMADA 2: APLICAÇÃO / LÓGICA DE NEGÓCIO (faz o papel do PHP no Apache) ----------
def processar_compra(codigo, qtd):
    """Aplica as regras. Não sabe como o dado é guardado nem como é exibido."""
    livro = buscar_livro(codigo)
    if livro is None:
        return {"ok": False, "motivo": "Livro não encontrado"}
    if livro["estoque"] < qtd:
        return {"ok": False, "motivo": f"Estoque insuficiente de {livro['titulo']}"}
    total = livro["preco"] * qtd
    if qtd >= 3:                 # regra de negócio: 10% de desconto a partir de 3 unidades
        total *= 0.9
    baixar_estoque(codigo, qtd)
    return {"ok": True, "titulo": livro["titulo"], "total": total}

# ---------- CAMADA 1: APRESENTAÇÃO (faz o papel do HTML/CSS/JS no navegador) ----------
def tela_de_compra(codigo, qtd):
    """Só mostra. Não calcula desconto nem acessa o banco."""
    print(f"\n[Cliente] Quero {qtd}x do livro {codigo}")
    resposta = processar_compra(codigo, qtd)
    if resposta["ok"]:
        print(f"  OK: {resposta['titulo']} por R$ {resposta['total']:.2f}")
    else:
        print(f"  ERRO: {resposta['motivo']}")

tela_de_compra("L01", 3)   # compra com desconto
tela_de_compra("L01", 1)   # o estoque acabou na compra anterior
tela_de_compra("L02", 1)   # sem estoque
tela_de_compra("X99", 1)   # livro inexistente