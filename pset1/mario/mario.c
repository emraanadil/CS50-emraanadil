#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Getting User input ;
    int input;
    do
    {
        input = get_int("Height: ");
    }
    while (input > 8 || input < 1);

    //Logic for building hashes;
    for (int i = 0; i < input; i++)
    {
        //printing spaces
        for (int s = input - 1; s > i; s--)
        {
            printf(" ");
        }

        for (int n = 0; n < i; n++)
        {
            printf("#");
        }
        printf("#\n");
    }










}