// intro-programacao/desconto.c
// Caixa de mercado: 10% de desconto em compras de R$ 100 ou mais.
#include <stdio.h>

int main(void)
{
    float total;

    printf("Total da compra: R$ ");
    scanf("%f", &total);                        // Leia total

    if (total >= 100)                           // Se total >= 100 Então
    {
        total = total * 0.9;                    //   total ← total * 0,9
    }                                           // Fim Se

    printf("Valor a pagar: R$ %.2f\n", total);  // Escreva total
    return 0;
}                                               // Fim