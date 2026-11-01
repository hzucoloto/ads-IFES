#include <stdio.h>

int main(void)

{
    // declaração da operação
    int operador;

    // declaração de números para cálculo
    float num1;
    float num2;

    // declaração de resultado
    float result;

    // escolha da operação
    printf("Qual operação você quer executar?\nDigite 1 para adição, 2 para subtração, 3 para multiplicação e 4 para divisão.\n");
    scanf("%d", &operador);

    // escolha dos números para operar
    printf("Agora, escolha dois números para essa operação:\n");
    scanf("%f %f", &num1, &num2);

    // cálculo de acordo com a operação selecionada
    switch (operador)
    {
    case 1:
        result = num1 + num2;
        printf("O resultado de sua operação é: %.1f\n", result);
        break;

    case 2:
        result = num1 - num2;
        printf("O resultado de sua operação é: %.1f\n", result);
        break;

    case 3:
        result = num1 * num2;
        printf("O resultado de sua operação é: %.1f\n", result);
        break;

    case 4:
        if (num2 == 0)
        {
            printf("Não é possível dividir por zero.\n");
        }
        else
        {
            result = num1 / num2;
            printf("O resultado de sua operação é: %.1f\n", result);
        }
        break;

    default:
        printf("Operação Inválida!\n");
        break;
    }

    return 0;
}