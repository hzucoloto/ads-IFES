#include <stdio.h>

int main(void)
{
    // definir o dia da semana e perguntar
    int dia;

    printf("Digite um número para o dia da semana desejado\n");
    scanf("%d", &dia);

    // com base na resposta, imprimir o dia
    switch (dia)
    {
    case 1:
        printf("Domingo\n");
        break;

    case 2:
        printf("Segunda\n");
        break;

    case 3:
        printf("Terca\n");
        break;

    case 4:
        printf("Quarta\n");
        break;

    case 5:
        printf("Quinta\n");
        break;

    case 6:
        printf("Sexta\n");
        break;

    case 7:
        printf("Sabado\n");
        break;

    default:
        printf("Dia Incorreto\n");
        return 0;
    }

    return 0;
}
