#include <stdio.h>

int main(void)
{
    // Declaração: int porque os números serão inteiros
    int altura, base, area;

    // Entrada: perguntar altura e perguntar base
    printf("Qual a altura desejada em centímetros? ");
    scanf("%d", &altura);
    printf("Qual a base desejada em centímetros? ");
    scanf("%d", &base);

    // Processamento: realizar o cálculo da área (b * h)
    area = altura * base;

    // Saída: diz a área do retângulo em cm²
    printf("A área do seu retângulo é: %d cm²\n", area);

    return 0;

}