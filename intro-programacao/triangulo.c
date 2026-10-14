#include <stdio.h>

int main() {
    // define os lados
    float a, b, c;

    // armazena os lados pela variável real, aceitando números decimais
    scanf("%f %f %f", &a, &b, &c);

    // verifica a condição para que as variáveis formem ou não um triângulo
    if (a < b + c && b < a + c && c < a + b) {
        printf("SIM\n");
    } else {
        printf("NAO\n");
    }

    return 0;
}