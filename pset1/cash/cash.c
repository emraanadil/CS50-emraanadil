#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    // getting user input;
    float input;
    do
    {
        input = get_float("Money in Dollars:");
    }
    while (input < 0);

    //converting dollars into cents
    int cents = round(input * 100);

    //how many quarters;
    int cents_25 = 0;
    while (cents >= 25)
    {
        cents_25 ++;
        cents -= 25;
    }
    // how many 10s;
    int cents_10 = 0;
    while (cents >= 10)
    {
        cents_10 ++;
        cents -= 10;
    }
    // how many 5a;
    int cents_5 = 0;
    while (cents >= 5)
    {
        cents_5 ++;
        cents -= 5;
    }
    // how many pennies;
    int cents_1 = 0;
    while (cents >= 1)
    {
        cents_1 ++;
        cents -= 1;
    }


    //print the no of coins;
    int sum = cents_25 + cents_10 + cents_5 + cents_1;
    printf("%i\n", sum);
}