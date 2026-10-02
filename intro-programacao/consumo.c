#include <stdio.h>

int main(void)
{
    // 1. Declaração: float porque consumo tem casas decimais
    float km, litros, consumo;

    // 2. Entrada
    printf("Quilometros rodados: ");
    scanf("%f", &km);
    printf("Litros abastecidos: ");
    scanf("%f", &litros);

    // 3. Processamento
    consumo = km / litros;

    // 4. Saida
    printf("Consumo medio: %.2f km/l\n", consumo);
    return 0;
}