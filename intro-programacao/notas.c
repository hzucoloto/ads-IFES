#include <stdio.h>

int main(void)
{
    int quantidade;

    // do-while: pergunta PELO MENOS UMA VEZ e repete enquanto o valor for inválido
    do
    {
        printf("Quantos alunos fizeram a prova? ");
        scanf("%d", &quantidade);
        if (quantidade <= 0)
        {
            printf("Valor inválido, tente de novo.\n");
        }
    }
    while (quantidade <= 0);   // <- o ponto e vírgula é obrigatório aqui

    // while: testa ANTES de cada volta
    int aluno = 1;                 // inicializa antes do laço
    while (aluno <= quantidade)
    {
        printf("Lançando nota do aluno %d\n", aluno);
        aluno++;                   // sem esta linha: laço infinito
    }

    printf("Fim da chamada.\n");
    return 0;
}