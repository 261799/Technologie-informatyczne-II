#include <iostream>
#define SIZE 10

void printArray(int numbers[], int size) {
    for (int i = 0; i < size; ++i) {
        printf("numbers[%d] = %d\n", i, numbers[i]);
    }
}

void menu(void) {
    printf("1. Wpisz wartosci do tablicy\n");
    printf("2. Wyswietl zawartosc tablicy\n");
    printf("3. Okresl najmniejsza wartosc tablicy\n");
    printf("4. Okresl najwieksza wartosc tablicy\n");
    printf("5. Okresl wartosc srednia\n");
    printf("0. Wyjscie\n");
    printf("Wybierz opcje:\n");
}
void funkcjawpisywanie (int numbers[], int size) {
    for (int i = 0; i < SIZE; i++) {
        printf("numbers[%d] = ", i);
        scanf_s("%d", &numbers[i]);
    }
}
int funkcjaminimum (int numbers[], int size)
{
    int min = numbers[0];
    for (int i = 0; i < size; i++)
    {
        if (min > numbers[i])
        {
            min = numbers[i];
        }
    }
    return min;
}
int funkcjamaximum (int numbers[], int size)
{

    int max = numbers[0];
    for (int i = 0; i < size; i++)
    {
        if (max < numbers[i])
        {
            max = numbers[i];
        }
    }
    return max;
}
int funkcjasrednia (int numbers[], int size) {
    float suma = 0;
    for (int i = 0; i < size; i++) {
        suma += numbers[i];
    }
    return suma / size;
}

int main() {
    int numbers[SIZE] = {1, 2, 3, -4, 50, 6, 7, 8, 9, 10};
    int option = 0;

    printf("PROSTA TABLICA\n\n");

    do {
        menu();
        scanf("%d", &option);

        switch (option) {
            case 0:
                break;
            case 1:
                funkcjawpisywanie(numbers, SIZE );
                break;
            case 2:
                printArray(numbers, SIZE);
                break;
            case 3:
                printf("Okreslanie najmniejszej wartosci\n\n");
                printf("min = %d\n", funkcjaminimum(numbers, SIZE));
                break;
            case 4:
                printf("Okreslanie najwiekszej wartosci\n\n");
                printf("max = %d\n",funkcjamaximum(numbers, SIZE));
                break;
            case 5:
                printf("Okreslanie wartosci sredniej\n\n");
                printf("srednia = %d\n", funkcjasrednia(numbers, SIZE));
                break;
            default:
                printf("Wybierz poprawna opcje...\n\n");
        }

    } while (option != 0);


    printf("THE END!\n");

    return 0;
}
