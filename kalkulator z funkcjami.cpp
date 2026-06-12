#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float sum(float, float);
float substraction(float, float);
float multiply(float, float);
float division(float, float);

float result;
float number1;
float number2;

int main(void)
{

	printf("Wprowadz wartosc pierwszej zmiennej:\n");
	scanf_s("%f", &number1);
	printf("Wprowadz wartosc drugiej zmiennej: \n");
	scanf_s("%f", &number2);

	printf("Wybierz dzialanie ktore chcesz uzyc i wcisnij odpowiadajaca jemu cyfre:\n" " 1. Dodawanie \n 2. Odejmowanie \n 3. Mnozenie \n 4. Dzielenie \n");
	int w;
	scanf_s("%d", &w);

	switch (w)
	{
	case 1:
		result = sum(number1, number2);
		printf("Wynik dodawania: %f \n", result);
		break;
	case 2:
		result = substraction(number1, number2);
		printf("Wynik odejmowania: %f \n", result);
		break;
	case 3:
		result = multiply(number1, number2);
		printf("Wynik mnożenia %f \n", result);
		break;
	case 4:
		result = division(number1, number2);
		printf("Wynik dzielenia: %f \n", result);
		break;
		}
	system("pause");
}


float sum(float number1, float number2)
{
	float result = number1 + number2;
	return result;
}

float substraction(float number1, float number2)
{
	float result = number1 - number2;
	return result;
}
float multiply(float number1, float number2)
{
	float result = number1 * number2;
	return result;
}
float division(float number1, float number2)
{
	if (number2 == 0)
	{
		printf("Nie dziel przez 0 \n");
		system("pause");
	}
	else
	{
		float result = number1 / number2;
		return result;
	}
}
