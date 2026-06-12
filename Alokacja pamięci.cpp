#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main() {
    time_t t;
    int iloscLiczb=0;
    int highest=0;
    int lowest=0;
    int * randomNums;

    printf("Ile liczb losowych potrzebujesz?\n");
    scanf("%d", &iloscLiczb);
    printf("Podaj dolny prog\n");
    scanf("%d", &lowest);
    printf("Podaj gorny prog\n");
    scanf("%d", &highest);
    if (highest<lowest)
    {
        printf("Blednie wyznaczyles progi");
        exit(2);
    }

    srand(time(&t));
    randomNums = (int *) calloc(iloscLiczb, sizeof(int));

if (randomNums==NULL)
    {
        printf("Nie udało się alokować tablicy!\n");
        exit(1);
    }
    for (int i = 0; i < iloscLiczb; i++)
    {
        randomNums[i] = (rand() % (highest-lowest+1) + lowest);
        printf("%d \n", randomNums[i]);
    }

    while(1)
    {
        printf("A ile teraz chcesz cwaniaczku?????\n");
        scanf("%d", &iloscLiczb);
        if (iloscLiczb==0)
        {
            break;
        }
        realloc(randomNums, iloscLiczb );

        if (randomNums==NULL)
        {
            printf("Nie udało się realokować tablicy!\n");
            exit(3);
        }
        for (int i = 0; i < iloscLiczb; i++)
        {
            randomNums[i] = (rand() % (highest-lowest+1) + lowest);
            printf("%d \n", randomNums[i]);
        }
    }
    free(randomNums);
    return(0);
}

