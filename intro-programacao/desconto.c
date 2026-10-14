#include <stdio.h>

int main(void)
{
    float total;

    // solicita o total de compra e grava o valor
    printf("Total da compra: R$ ");
    scanf("%f", &total);

    // expressão condicional de true or false
    if (total >= 100)
    {
        float desconto = total * 0.10; // para gerar os 10% de desconto
        printf("Desconto de: R$ %.2f\n", desconto);
        printf("Total a pagar: R$ %.2f\n", total - desconto);
    }
    else
    {
        printf("Faltam R$ %.2f para ganhar 10%%.\n", 100 - total);
        printf("Total a pagar: R$ %.2f\n", total);
    }
    return 0;
}
