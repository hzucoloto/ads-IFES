# Simula um pipeline CI/CD de uma loja virtual.
# Cada etapa retorna True (passou) ou False (falhou).

def calcular_frete(peso_kg, distancia_km):
    """Regra de negócio da loja (trabalho do Back-End)."""
    return 10 + peso_kg * 2 + distancia_km * 0.05

def etapa_build():
    return True  # aqui o código seria empacotado (ex.: imagem Docker)

def etapa_testes():
    # Trabalho do QA: um pedido de 2 kg a 100 km deve custar 19.0
    return calcular_frete(2, 100) == 19.0

def etapa_seguranca():
    return True

def etapa_deploy():
    return True  # aqui a versão iria para o servidor de produção

pipeline = [("Build", etapa_build),
            ("Testes", etapa_testes),
            ("Segurança", etapa_seguranca),
            ("Deploy", etapa_deploy)]

for nome, etapa in pipeline:
    passou = etapa()
    print(f"[{'OK' if passou else 'FALHOU'}] {nome}")
    if not passou:
        print("Pipeline interrompido: nada vai para produção.")
        break
else:  # o else do for só roda se o loop terminou sem break
    print("Versão publicada em produção!")