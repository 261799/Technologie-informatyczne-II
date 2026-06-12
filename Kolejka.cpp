//
// Created by student on 11.05.2026.
//
//#include <iostream>
#include <stdio.h>
#include "Stack.cpp"


void menu(void)
{
    printf("\n");
    printf("1 - wstaw liczbe do kolejki \n");
    printf("2 - odczytaj wartosc z poczatku kolejki \n");
    printf("3 - usun liczbe z kolejki \n");
    printf("4 - sprawdz czy kolejka jest pusta \n");
    printf("5 - sprawdz czy kolejka jest pelna \n");
    printf("6 - koniec programu \n");
    printf("\n");
}

int main()
{
    int temp = 0;
    int option = 0;
    printf("KOLEJKA - implementacja w tablicy statycznej\n");
    while (1)
    {
        menu();
        scanf("%d", &option);


        switch (option)
        {
            case 1:
                if ( !isQueueFull() ){
                    printf("Podaj wartosc: ");
                    scanf("%d", &temp);
                    Wstaw(temp);
                }
                else {
                    printf("operacja niedozwolona KOLEJKA pelna!!!\n\n");
                }

                break;

            case 2:
                if (!isQueueEmpty()) {
                    temp = Odczytaj();
                    printf("Odczytana wartosc: %d", temp);
                }
                else {
                    printf("operacja niedozwolona KOLEJKA pusta!!!\n\n");
                }

                break;

            case 3:
                if (!isQueueEmpty()) {
                    temp = Usun();
                    printf("Odczytana wartosc: %d", temp);
                }
                else {
                    printf("operacja niedozwolona KOLEJKA pusta!!!\n\n");
                }
                break;

            case 4:
                if (isQueueEmpty()) {
                    printf("KOLEJKA jest pusta.\n");
                }
                else {
                    printf("KOLEJKA nie jest pusta.\n");
                }
                break;

            case 5:
                if (isQueueFull()) {
                    printf("KOLEJKA jest pelna.\n");
                }
                else {
                    printf("KOLEJKA nie jest pelna.\n");
                }
                break;

            case 6:
                //zakonczenie programu
                return 0;

            default:
                printf("Wybierz wlasciwa opcje.\n\n");
                break;
        }
    }

    return 0;
}
