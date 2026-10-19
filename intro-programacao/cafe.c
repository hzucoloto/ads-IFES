// intro-programacao/cafe.c
// O algoritmo do café dos slides, mas com quantidades exatas:
// o computador não aceita "um pouco de água".
#include <stdio.h>

int main(void)
{
    int xicaras;

    // Entrada: o dado que o algoritmo precisa
    printf("Quantas xícaras de café? ");
    scanf("%d", &xicaras);

    // Processamento: transformar a entrada em quantidades precisas
    int agua_ml = xicaras * 100;  // 100 ml por xícara
    int po_g = xicaras * 8;       // cerca de 8 g de pó por xícara

    // Saída: os passos, em ordem
    printf("1. Coloque %d ml de água na chaleira.\n", agua_ml);
    printf("2. Ligue o fogão e aqueça a água.\n");
    printf("3. Coloque %d g de pó no filtro.\n", po_g);
    printf("4. Despeje a água quente sobre o pó.\n");
    printf("5. Aguarde o café passar.\n");
    printf("6. Sirva %d xícara(s).\n", xicaras);

    return 0;
}