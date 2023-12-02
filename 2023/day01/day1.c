#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main() {

    FILE *fptr;
    unsigned long filesize;
    char *buffer;

    fptr = fopen("input.txt","r");
    if(fptr == NULL)    {
        printf("ERROR: Unable to open file.\n");
        return 1;             
    }

    // Moves the cursor to the end of the file

    fseek(fptr, 0L, SEEK_END);
    filesize = ftell(fptr);
    fseek(fptr, 0L, SEEK_SET);

    buffer = malloc(filesize+1);
    if (buffer == NULL) {
        printf("ERROR: Unable allocate memory\n");
        fclose(fptr);
        return 1;
    }

    size_t n = fread(buffer, 1, filesize, fptr);
    if (n != filesize) {
        printf("ERROR: Failed to read file.\n");
        free(buffer);
        fclose(fptr);
        return 1;
    }

    buffer[filesize] = '\0';


    char first = NULL;
    char last = NULL;
    unsigned int total = 0;
    for (unsigned long count = 0;count < filesize;count++) {
        char temp = buffer[count];
        if (temp == '\n') {
            if (last == NULL) {
                last = first;
            }
            char number_string[2];
            number_string[0]=first;
            number_string[1]=last;
            unsigned int number = atoi(number_string);
            total = total + number;

            //printf("%d\n",number);
            first = NULL;
            last = NULL;
        }
        if ( isdigit(temp) ) {
            if (first == NULL) {
                first = temp;
            } else {
                last = temp;
            }

        }
    }

    printf("Total: %d\n",total);

    //printf("%s",buffer);

    fclose(fptr);
    free(buffer);
    return 0;
}
