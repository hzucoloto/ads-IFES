# include <stdio.h>

int main(void)

{
    // Declaração: total de vagas, carros que entraram, carros que saíram
    int vagas, carin, carout, vagasfim;

    // Entrada de informações
    printf("Quantas vagas há no estacionamento? ");
    scanf("%d", &vagas);
    printf("Quantos carros entraram? ");
    scanf("%d", &carin);
    printf("Quantos carros saíram? ");
    scanf("%d", &carout);

    // Processamento de informações
    vagasfim = vagas - carin + carout;

    // Saída: mostra as vagas após entrada e saída de carros
    printf("Existem %d vagas no estacionamento.\n", vagasfim);

    return 0;
}