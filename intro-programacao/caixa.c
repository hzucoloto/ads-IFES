#include <stdio.h>

int main(void)
{
    float total;
    int pagamento;

    printf("Total da compra: R$ ");
    scanf("%f", &total);

    // operador NÃO: "se NÃO for maior que zero"
    if (!(total > 0))
    {
        printf("Valor invalido\n");
        return 1;
    }

    printf("Pagamento (1-Dinheiro, 2-Debito, 3-Credito): ");
    scanf("%d", &pagamento);

    // switch: escolhe UMA opção a partir de um valor inteiro
    switch (pagamento)
    {
        case 1:
            printf("Dinheiro\n");
            // condição composta com E: as duas precisam ser verdadeiras
            if (total >= 100 && total <= 1000)
            {
                total = total * 0.90;
                printf("Desconto de 10%% aplicado!\n"); // %% imprime o símbolo %
            }
            break;
        case 2:
            printf("Debito\n");
            break;
        case 3:
            printf("Credito\n");
            // condição aninhada (está dentro do case) e composta com OU
            if (total < 20 || total > 5000)
            {
                printf("Credito so entre R$ 20 e R$ 5000\n");
                return 1;
            }
            break;
        default:
            printf("Forma de pagamento invalida\n");
            return 1;
    }

    printf("Valor final: R$ %.2f\n", total);
    return 0;
}