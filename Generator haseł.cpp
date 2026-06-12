#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));
    int symbols = (rand() % 5) + 1;
    int numbers = (rand() % 5) + 1;
    int capital = (rand() % 5) + 1;
    int small = (rand() % 5) + 1;

    // printf("Wylosowane liczby:\n");
    // printf("symbols: %d\n", symbols);
    // printf("numbers: %d\n", numbers);
    // printf("capital: %d\n", capital);
    // printf("small: %d\n", small);

    int total_length = symbols + numbers + capital + small;
    char password[total_length + 1]; // +1 na znak końca ciągu '\0'
    int index = 0;

    for(int i = 0; i < symbols; i++) password[index++] = (rand() % 15) + 33;

    for(int i = 0; i < numbers; i++) password[index++] = (rand() % 10) + 48;

    for(int i = 0; i < capital; i++) password[index++] = (rand() % 26) + 65;

    for(int i = 0; i < small; i++) password[index++] = (rand() % 26) + 97;

    password[index] = '\0';

    for (int i = 0; i < total_length; i++) {
        int target = rand() % total_length;
        char temp = password[i];
        password[i] = password[target];
        password[target] = temp;
    }
    printf("Wygenerowane haslo: %s\n", password);

    return 0;
}
