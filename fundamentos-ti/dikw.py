# Dado -> Informação -> Conhecimento, usando uma regra de produção (SE... ENTÃO...)

# 1. DADOS: valores soltos, sem contexto
dados = ["Laura", "15/09/2025", 2300.00]
print("Dados:", dados)

# 2. INFORMAÇÃO: os mesmos dados, organizados e com significado
pagamento = {"nome": dados[0], "data": dados[1], "valor": dados[2]}
print(f"Informação: {pagamento['nome']} recebeu R$ {pagamento['valor']:.2f} em {pagamento['data']}.")

# 3. CONHECIMENTO representado como regra de produção
historico = [2300.00, 2300.00, 2300.00]  # pagamentos de julho, agosto e setembro
# SE recebe o mesmo valor há 3+ meses ENTÃO renda fixa
if len(historico) >= 3 and len(set(historico)) == 1:
    print("Conhecimento: renda fixa mensal -> perfil de menor risco para crédito.")
else:
    print("Conhecimento: renda variável -> analisar com mais cuidado.")