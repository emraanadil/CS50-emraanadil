#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

// define byte as 8 bits;
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }

    FILE *input_file = fopen(argv[1], "r");
    // checking for null file.
    if (input_file == NULL)
    {
        printf("Can't Open %s\n", argv[1]);
        return 2;
    }
    //initialize variablesss
    BYTE buffer[512];
    char file_name[8];
    bool open_img = false;
    FILE *output_file = NULL;
    int filenumber = 0;

    while (fread(buffer, 512, 1, input_file) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (!open_img)
            {
                open_img = true;
            }
            else
            {
                fclose(output_file);
            }
            sprintf(file_name, "%03i.jpg", filenumber++);
            output_file = fopen(file_name, "w");
            if (output_file == NULL)
            {
                printf("can't write into file");
                return 1;
            }
            fwrite(buffer, 512, 1, output_file);

        }

        else if (open_img)
        {
            fwrite(buffer, 512, 1, output_file);
        }



    }

}
// //
// // 1.open memorycard
// 2.repeat until end of card