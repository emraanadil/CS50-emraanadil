#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

//Delcaring the prototype;
int count_letters(string word);
int count_words(string word);
int count_sentences(string word);

int main(void)
{
    //getting user input;
    string input = get_string("Text: ");
    float letters = count_letters(input);
    float words = count_words(input);
    float L = ((letters / words) * 100);
    float sentences = count_sentences(input);
    float S = ((sentences / words) * 100);
    // coleman lieu index formula;
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    //printing the grade;
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

}
//fnction for the count of letters;
int count_letters(string word)
{
    int letters = 0;

    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isalpha(word[i])) //checking for the alphabet;
        {
            letters++;
        }
    }
    return letters;
}

// count the no of words
int count_words(string word)
{
    int words = 0;
    if (strlen(word) > 1)
    {
        words = 1;
    }
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isspace(word[i])) //checking white spaces
        {
            words++;
        }
    }
    return words;
}
// coutnig the no of sentences
int count_sentences(string word)
{
    int sentences = 0;
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (word[i] == '?' || word[i] == '!' || word[i] == '.')
        {
            sentences++;
        }
    }
    return sentences;
}