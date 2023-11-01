#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include "stdlib.h"

//declaring pseudo fuctions to check whether string is all digit;
int checkdigit(string input);
int ciphertext(string input);

int key;


int main(int argc, string argv[])
{
    if (argc == 2)
    {
        //check the key using checkdigit fuction;
        if (checkdigit(argv[1]) == 0)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        else
        {
            // validated the key?/
            //converting the string key into int key;
            key = atoi(argv[1]);
            printf("%i\n", key);
            string text = get_string("plaintext: ");
            ciphertext(text);


        }


    }
    //if argc is not 2 we print erroe;
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }


}
//fuction;
int checkdigit(string input)
{
    for (int i = 0, len = strlen(input); i < len; i++)
    {
        if (isdigit(input[i]) == 0)
        {
            return 0;
        }

    }

    return 1;
}

int ciphertext(string input)
{
    for (int i = 0, len = strlen(input); i < len; i++)
    {

        if (isalpha(input[i]))
        {
            if (isupper(input[i]))//checking for upper case
            {
                input[i] = 65 + (((input[i] - 65) + key) % 26);
            }
            else //checking for lower case;
            {
                input[i] = 97 + (((input[i] - 97) + key) % 26);
            }
        }
        else
        {
            input[i] = input[i]; //for symbols;
        }
    }
    printf("ciphertext: %s\n", input);
    return 1;

}