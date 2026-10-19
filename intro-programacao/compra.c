#include <stdio.h>   // [complemento] traz printf e scanf (faltou no slide)

int main(void)       // 1. Início do programa (o slide usa int main(), também vale)
{
    // 2. Declaração de variáveis
    float preco, desconto, valor;

    // 3. Entrada de dados
    printf("Preço do produto: R$ ");
    scanf("%f", &preco);              // & = "guarde no endereço de preco"
    printf("Desconto: R$ ");
    scanf("%f", &desconto);

    // 4. Processamento
    valor = preco - desconto;

    // 5. Saída de dados
    printf("O valor da compra é R$ %.2f\n", valor);  // [complemento] %.2f = 2 casas; \n = quebra de linha

    return 0;        // 6. Fim do programa
}