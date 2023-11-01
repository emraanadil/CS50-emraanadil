#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Start Size:
    int n;
    do
    {
        n = get_int("Start Size: ");
    }
    while (n < 9);

    // End Size:

    int e;
    do
    {
        e = get_int("End Size: ");
    }
    while (e < n);

// No of Years:

    int y = 0;
    while (n < e)
    {
        n = n + (n / 3) - (n / 4);
        y++;
    }

    //Print;

    printf("Years: %i\n", y);

}