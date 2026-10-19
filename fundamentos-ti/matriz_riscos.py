# Priorização de riscos: probabilidade x impacto (item 3.4 do livro)
PROB = {"baixa": 1, "média": 2, "alta": 3}
IMPACTO = {"leve": 1, "moderado": 2, "grave": 3, "catastrófico": 4}

riscos = [
    ("Dev sênior sai da empresa", "média", "grave", "Mitigar"),
    ("Cliente muda requisitos toda semana", "alta", "moderado", "Mitigar"),
    ("Nova lei de proteção de dados (LGPD)", "baixa", "grave", "Aceitar"),
    ("Servidor próprio sem redundância", "média", "catastrófico", "Transferir"),
]

# nota = probabilidade x impacto; maior nota = atacar primeiro
tabela = sorted(riscos, key=lambda r: PROB[r[1]] * IMPACTO[r[2]], reverse=True)

for nome, p, i, estrategia in tabela:
    nota = PROB[p] * IMPACTO[i]
    alerta = "🔴 PRIORIDADE" if nota >= 6 else ""
    print(f"{nota:>2} | {nome:<40} | {p:<6} x {i:<12} → {estrategia} {alerta}")