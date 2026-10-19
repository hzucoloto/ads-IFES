#include <stdio.h>

#define DESCONTO 0.10            // constante simbólica: o pré-processador troca DESCONTO por 0.10
const float TAXA_SACOLA = 0.25;  // [complemento] constante tipada: o compilador proíbe alterar

int total_atendimentos = 0;      // GLOBAL: visível em todo o arquivo

void atender_cliente(float valor)
{
    static int senha = 0;        // ESTÁTICA: inicializada uma vez só; o valor sobrevive entre chamadas
    int senha_local = 0;         // LOCAL: recriada (e zerada) a cada chamada

    senha++;
    senha_local++;
    total_atendimentos++;

    float a_pagar = valor - valor * DESCONTO + TAXA_SACOLA;
    printf("Senha estática: %d | senha local: %d | a pagar: R$ %.2f\n",
           senha, senha_local, a_pagar);
}

int main(void)
{
    float compra;
    printf("Valor da compra: ");
    scanf("%f", &compra);

    atender_cliente(compra);
    atender_cliente(compra);
    atender_cliente(compra);

    printf("Total de atendimentos (global): %d\n", total_atendimentos);

    // printf("%d\n", senha);     // descomente: erro! 'senha' só existe dentro de atender_cliente
    // TAXA_SACOLA = 0.50;        // descomente: erro! não dá para alterar uma const
    return 0;
}