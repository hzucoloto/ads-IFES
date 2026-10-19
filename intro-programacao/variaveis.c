#include <stdio.h>
#include <stdbool.h>   // [complemento] necessário para usar bool

int main(void)
{
    // Declaração + inicialização
    int quantidade = 3;            // inteiro
    float preco_unitario = 4.50;   // real (ponto, não vírgula!)
    char categoria = 'B';          // UM caractere: aspas simples
    char cliente[] = "Ana";        // "cadeia": em C é vetor de char
    bool tem_desconto = true;      // lógico

    // Atribuição: substitui o valor anterior
    quantidade = quantidade + 2;   // agora vale 5
    quantidade++;                  // agora vale 6

    float total = quantidade * preco_unitario;

    printf("Cliente: %s (categoria %c)\n", cliente, categoria);
    printf("Itens: %i | Total: R$ %.2f\n", quantidade, total);
    printf("Desconto? %i\n", tem_desconto);       // mostra 1 (verdadeiro)

    // Pegadinha da divisão
    printf("1000 / 12   = %i\n", 1000 / 12);      // inteiro / inteiro
    printf("1000 / 12.0 = %.2f\n", 1000 / 12.0);  // um lado real -> resultado real
    return 0;
}