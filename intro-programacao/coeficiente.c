#include <stdio.h>

int main(void)
{
    int quantidade;
    float nota, carga;
    float soma_ponderada = 0;   // soma de (nota * carga horária)
    float soma_cargas = 0;      // soma das cargas horárias

    printf("Quantas disciplinas o aluno cursou? ");
    scanf("%d", &quantidade);

    // for: repete exatamente "quantidade" vezes (laço determinado)
    for (int i = 1; i <= quantidade; i++)
    {
        printf("Nota da disciplina %d: ", i);
        scanf("%f", &nota);
        printf("Carga horária da disciplina %d: ", i);
        scanf("%f", &carga);

        soma_ponderada = soma_ponderada + nota * carga;
        soma_cargas = soma_cargas + carga;
    }

    if (soma_cargas > 0)   // evita divisão por zero
    {
        float cr = soma_ponderada / soma_cargas;
        printf("CR = %.2f\n", cr);
    }
    else
    {
        printf("CR = 0.00\n");
    }
    return 0;
}