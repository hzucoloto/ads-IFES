# fundamentos-ti/tipos_si.py
# Os MESMOS dados de vendas de uma rede de farmácias passando pela pirâmide de SIs.
# TPS registra -> SIG resume -> SAD simula -> SAE mostra poucos indicadores.

# ---------- TPS / SPT (operacional): registra CADA transação ----------
vendas = []  # o "banco de dados" alimentado pelo caixa


def registrar_venda(dia, filial, produto, valor):
    """Uma transação = um registro. Alto volume, rápido, padronizado."""
    vendas.append({"dia": dia, "filial": filial, "produto": produto, "valor": valor})


# ---------- SIG / MIS (tático): relatório periódico e agregado ----------
def relatorio_por_filial():
    """Não mostra cada venda: mostra o TOTAL. Olha para o passado."""
    totais = {}
    for venda in vendas:
        totais[venda["filial"]] = totais.get(venda["filial"], 0) + venda["valor"]
    return {filial: round(total, 2) for filial, total in totais.items()}


def relatorio_de_excecao(minimo):
    """Também é SIG: só avisa o que fugiu do padrão. Não simula nada."""
    return [filial for filial, total in relatorio_por_filial().items() if total < minimo]


# ---------- SAD / DSS (tático/estratégico): "e se...?" interativo ----------
def simular_reajuste(aumento_preco, queda_vendas):
    """Pergunta sobre o FUTURO: e se o preço subir X% e as vendas caírem Y%?"""
    atual = sum(v["valor"] for v in vendas)
    projetado = atual * (1 + aumento_preco / 100) * (1 - queda_vendas / 100)
    return atual, projetado


# ---------- SAE / EIS (estratégico): poucos KPIs para o executivo ----------
def painel_executivo(meta):
    """Visão de cima: 2 ou 3 números e um alerta, sem detalhe de cada venda."""
    total = sum(v["valor"] for v in vendas)
    ticket_medio = total / len(vendas)
    situacao = "ACIMA da meta" if total >= meta else "ABAIXO da meta"
    return {"faturamento": round(total, 2), "ticket médio": round(ticket_medio, 2), "situação": situacao}


def main():
    # O caixa (TPS) registra o dia a dia, venda por venda
    registrar_venda(1, "Vila Velha", "dipirona", 12.50)
    registrar_venda(1, "Vila Velha", "protetor solar", 64.90)
    registrar_venda(1, "Vitória", "vitamina C", 39.90)
    registrar_venda(2, "Serra", "dipirona", 12.50)
    registrar_venda(2, "Vitória", "fralda", 89.90)
    registrar_venda(2, "Vila Velha", "shampoo", 27.00)

    print("TPS -> transações registradas:", len(vendas))
    print("SIG -> total por filial:", relatorio_por_filial())
    print("SIG -> filiais abaixo de R$ 50 (relatório de exceção):", relatorio_de_excecao(50))

    # O SAD é interativo: o gerente digita o cenário que quer testar
    aumento = float(input("SAD -> aumento de preço (%): "))
    queda = float(input("SAD -> queda esperada nas vendas (%): "))
    atual, projetado = simular_reajuste(aumento, queda)
    print(f"SAD -> hoje R$ {atual:.2f} | no cenário R$ {projetado:.2f}")

    print("SAE -> painel do diretor:", painel_executivo(meta=300))


main()