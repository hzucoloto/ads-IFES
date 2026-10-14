#include <stdio.h>

int main(void)

{
    // definindo variáveis e armazenando os valores
    float base, altura;
    printf("Qual a base em cm? ");
    scanf("%f", &base);
    printf("Qual a altura em cm? ");
    scanf("%f", &altura);

    // calculo da area
    float area = base * altura;

    // traz mensagem caso seja quadrado ou retangulo
    printf("A área é: %.2f cm²\n", area);
    if (base == altura)
    {
        printf("Sua figura é um quadrado!\n");
    }
    else
    {
        printf("Sua figura é um retângulo!\n");
    }
    return 0;
}