# fundamentos-ti/unidades_medida.py
# Semana 4: O computador e suas unidades de medida
# Mostra na prática por que bit != byte e por que 1000 != 1024 muda o resultado.
# Rode com: python3 unidades_medida.py

BITS_POR_BYTE = 8

# Base 10 (SI): usada por fabricantes de HD/SSD e por redes (Mbps)
DECIMAL = {"KB": 10**3, "MB": 10**6, "GB": 10**9, "TB": 10**12}
# Base 2 (IEC): usada pela RAM e pelo Windows (que escreve "GB", mas calcula em GiB)
BINARIO = {"KiB": 2**10, "MiB": 2**20, "GiB": 2**30, "TiB": 2**40}


def bytes_para(valor_bytes, unidade):
    """Converte uma quantidade de bytes para a unidade pedida."""
    tabela = {**DECIMAL, **BINARIO}
    return valor_bytes / tabela[unidade]


def mbps_para_mb_s(mbps):
    """Velocidade do plano (megaBITS/s) -> velocidade de download (megaBYTES/s)."""
    return mbps / BITS_POR_BYTE


def tempo_download(tamanho_mb, velocidade_mbps):
    """Segundos para baixar um arquivo: primeiro passa MB para Mb (x8), depois divide."""
    megabits = tamanho_mb * BITS_POR_BYTE
    return megabits / velocidade_mbps


def combinacoes(bits):
    """Cada bit dobra as possibilidades: N bits -> 2^N valores."""
    return 2 ** bits


if __name__ == "__main__":
    print("1) Quantos valores diferentes cabem em N bits (2^N)")
    for n in (1, 4, 8, 32):
        print(f"   {n:>2} bits -> {combinacoes(n):,} combinações".replace(",", "."))

    print("\n2) O 'HD que encolheu': etiqueta de 1 TB lida pelo Windows")
    hd = 1 * DECIMAL["TB"]
    print(f"   Fabricante (base 10): {bytes_para(hd, 'GB'):.0f} GB")
    print(f"   Windows    (base 2) : {bytes_para(hd, 'GiB'):.2f} GiB (mas aparece escrito 'GB')")

    print("\n3) Plano de internet: Mbps -> MB/s (divide por 8)")
    for plano in (100, 300, 500, 660, 750):
        print(f"   {plano} Mbps -> {mbps_para_mb_s(plano):.1f} MB/s")

    print("\n4) Baixar um jogo de 50 GB (50.000 MB) num plano de 750 Mbps")
    seg = tempo_download(50 * 1000, 660)
    print(f"   {seg:.0f} s ≈ {seg / 60:.1f} min (teórico, sem perdas da rede)")