# Simula dois pilares da Tríade CIA:
#   Integridade       -> hash (uma "impressão digital" do dado)
#   Confidencialidade -> cifra (esconde o conteúdo de quem não tem a chave)
import hashlib


def impressao_digital(texto):
    """Hash SHA-256 do texto (só os 16 primeiros caracteres)."""
    return hashlib.sha256(texto.encode()).hexdigest()[:16]


def cifra_de_cesar(texto, chave):
    """Cifra didática: desloca cada letra 'chave' posições. NÃO é segura."""
    resultado = ""
    for letra in texto:
        if letra.isalpha() and letra.isascii():
            base = ord("A") if letra.isupper() else ord("a")
            resultado += chr((ord(letra) - base + chave) % 26 + base)
        else:
            resultado += letra
    return resultado


# INTEGRIDADE: mudar 1 caractere muda o hash inteiro
pix_enviado = "PIX para Maria Souza: R$ 150,00"
pix_recebido = "PIX para Maria Souza: R$ 150,00"
print("Íntegro?", impressao_digital(pix_enviado) == impressao_digital(pix_recebido))

# CONFIDENCIALIDADE: sem a chave, o dado é ilegível
guardado = cifra_de_cesar("Paciente Joao Lima: diabetes tipo 2", 7)
print("Invasor vê:", guardado)
print("Médico lê:", cifra_de_cesar(guardado, -7))