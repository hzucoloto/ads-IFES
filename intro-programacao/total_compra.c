#include <stdio.h>

int main(void)
{
    float preco;
    float total = 0;   // acumulador: começa em 0, antes do laço

    do
    {
        printf("Preço do produto (0 para encerrar): ");
        scanf("%f", &preco);

        if (preco > 0)
        {
            total = total + preco;   // só soma os positivos
        }
        // negativos: não faz nada, apenas volta ao início do laço
    }
    while (preco != 0);   // o 0 encerra a repetição

    printf("Total da compra: R$ %.2f\n", total);
    return 0;
}