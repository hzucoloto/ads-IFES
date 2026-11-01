#include <stdio.h>

int main(void)

{
    // declara as variáveis
    int numa;
    int numb;
    int numc;

    // imprime frase inicial e armazena variáveis
    printf("Digite três números inteiros\n");
    scanf("%d", &numa);
    scanf("%d", &numb);
    scanf("%d", &numc);

    // classifica a ordem das variáveis
    // a < b < c 
    if ((numa <= numb) && (numb <= numc))
    {
        printf("%d, %d, %d\n", numa, numb, numc);
    }
    // a < c < b 
    else if ((numa <= numc) && (numc <= numb))
    {
        printf("%d, %d, %d\n", numa, numc, numb);
    }
    // b < a < c 
    else if ((numb <= numa) && (numa <= numc))
    {
        printf("%d, %d, %d\n", numb, numa, numc);
    }
    // b < c < a
    else if ((numb <= numc) && (numc <= numa))
    {
        printf("%d, %d, %d\n", numb, numc, numa);
    }
    // c < a < b
    else if ((numc <= numa) && (numa <= numb))
    {
        printf("%d, %d, %d\n", numc, numa, numb);
    }
    // c < b < a: sobrou só este caso
    else
    {
        printf("%d, %d, %d\n", numc, numb, numa);
    }

    return 0;
}