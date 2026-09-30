# probabilidade-estatistica/sessao_somatorio_descritiva.py
# Semanas 4 e 5: somatório + estatística descritiva
# Rodar (dentro da pasta probabilidade-estatistica):
#   python3 sessao_somatorio_descritiva.py
# Precisa de:  pip install matplotlib

import random
import statistics as st
import matplotlib
matplotlib.use("Agg")  # no Codespace não há janela: só salvamos a imagem
import matplotlib.pyplot as plt

# ---------- PARTE 1: somatórios (amostra da aula: SSDs vendidos em 7 dias) ----------
x = [5, 6, 2, 9, 8, 2, 5]
n = len(x)

SS = sum(x)                      # Σ xi     (soma simples)
SQ = sum(xi ** 2 for xi in x)    # Σ xi²    (soma de quadrados)
QS = sum(x) ** 2                 # (Σ xi)²  (quadrado da soma)
print(f"n={n}  SS={SS}  SQ={SQ}  QS={QS}")

# ---------- PARTE 2: medidas descritivas: com Σ (à mão) x biblioteca statistics ----------
rol = sorted(x)                  # rol: x(1) <= x(2) <= ... <= x(n)
media = SS / n
var_def = sum((xi - media) ** 2 for xi in x) / (n - 1)   # pela definição
var_atalho = (SQ - SS ** 2 / n) / (n - 1)                # fórmula alternativa
dp = var_def ** 0.5
cv = 100 * dp / media

print(f"rol = {rol}")
print(f"média = {media:.2f}  (statistics: {st.mean(x):.2f})")
print(f"mediana = {st.median(x)}  modas = {st.multimode(x)}")
print(f"variância: definição = {var_def:.3f} | atalho = {var_atalho:.3f} | statistics = {st.variance(x):.3f}")
print(f"desvio-padrão = {dp:.2f}  CV = {cv:.1f}%")

# ---------- PARTE 3: por que dividir por n-1? (simulação) ----------
random.seed(42)
populacao = [random.gauss(200, 40) for _ in range(10_000)]  # tempo de resposta de um site (ms)
sigma2 = st.pvariance(populacao)                             # parâmetro: divide por N

m, rodadas = 5, 5000             # amostras de 5 requisições, repetidas 5000 vezes
soma_n = soma_n1 = 0
for _ in range(rodadas):
    amostra = random.sample(populacao, m)
    xb = sum(amostra) / m
    desvios2 = sum((a - xb) ** 2 for a in amostra)
    soma_n += desvios2 / m           # dividindo por n
    soma_n1 += desvios2 / (m - 1)    # dividindo por n-1

print(f"\nvariância da população (parâmetro): {sigma2:.0f}")
print(f"média das estimativas dividindo por n  : {soma_n / rodadas:.0f}  <- subestima")
print(f"média das estimativas dividindo por n-1: {soma_n1 / rodadas:.0f}  <- acerta na média")

# ---------- PARTE 4: média x mediana (consumo de dados do Carlos, 24 meses) ----------
consumo = [19, 15, 15, 14, 22, 17, 17, 13, 13, 19, 11, 19,
           16, 17, 17, 33, 27, 18, 18, 22, 17, 19, 18, 17]

plt.hist(consumo, bins=range(10, 36, 2), edgecolor="black")
plt.axvline(st.mean(consumo), color="red", linestyle="--",
            label=f"média = {st.mean(consumo):.2f}")
plt.axvline(st.median(consumo), color="green",
            label=f"mediana = {st.median(consumo):.2f}")
plt.xlabel("Consumo mensal (GB)")
plt.ylabel("Nº de meses")
plt.title("Consumo de dados do Carlos")
plt.legend()
plt.savefig("consumo_carlos.png")
print("\nGráfico salvo em consumo_carlos.png")