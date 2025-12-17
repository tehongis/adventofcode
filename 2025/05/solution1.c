#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

/**
 * Does parse file and creates array ranges
 * missing comparing number into ranges
 * 
 */


 
size_t fileSize = 0;
char *fileBuffer = NULL;
char **lines = NULL;
size_t lineCount = 0;
size_t currentLineIndex = 0;

#define ARRAY_SIZE 1024
unsigned long int arrayBegin[ARRAY_SIZE];
unsigned long int arrayEnd[ARRAY_SIZE];

int arrayCount = 0;


bool read_input_file(void)
{
    FILE *file = fopen("input.txt", "r");
    if (file == NULL) {
        perror("Error opening input.txt");
        return false;
    }

    // Determine file size
    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    rewind(file);

    if (file_size < 0) {
        perror("Error determining file size");
        fclose(file);
        return false;
    }

    // Allocate memory for file contents (+ 1 for null terminator)
    fileBuffer = (char *)malloc(file_size + 1);
    if (fileBuffer == NULL) {
        perror("Memory allocation failed");
        fclose(file);
        return false;
    }

    // Read file into buffer
    fileSize = fread(fileBuffer, 1, file_size, file);
    if (fileSize != (size_t)file_size) {
        perror("Error reading file");
        free(fileBuffer);
        fclose(file);
        return false;
    }

    // Null-terminate the buffer
    fileBuffer[file_size] = '\0';

    fclose(file);
    return true;
}

/**
 * Resets the line iterator to the beginning.
 */
void reset_line_iterator(void)
{
    currentLineIndex = 0;
}

/**
 * Parses the file buffer into separate lines.
 * Allocates memory for the lines array and populates it.
 *
 * Returns: true on success, false on failure
 */
bool parse_lines(void)
{
    if (fileBuffer == NULL || fileSize == 0) {
        fprintf(stderr, "File buffer is empty or not initialized.\n");
        return false;
    }

    // Count the number of lines
    lineCount = 0;
    for (size_t i = 0; i < fileSize; i++) {
        if (fileBuffer[i] == '\n') {
            lineCount++;
        }
    }
    // Add 1 if the file doesn't end with a newline
    if (fileSize > 0 && fileBuffer[fileSize - 1] != '\n') {
        lineCount++;
    }

    if (lineCount == 0) {
        fprintf(stderr, "No lines found in file.\n");
        return false;
    }

    // Allocate memory for lines array
    lines = (char **)malloc(lineCount * sizeof(char *));
    if (lines == NULL) {
        perror("Memory allocation failed for lines array");
        return false;
    }

    // Parse lines
    size_t lineIdx = 0;
    size_t lineStart = 0;

    for (size_t i = 0; i <= fileSize; i++) {
        if (i == fileSize || fileBuffer[i] == '\n') {
            size_t lineLen = i - lineStart;
            
            // Allocate memory for this line
            lines[lineIdx] = (char *)malloc(lineLen + 1);
            if (lines[lineIdx] == NULL) {
                perror("Memory allocation failed for line");
                return false;
            }

            // Copy line content
            strncpy(lines[lineIdx], &fileBuffer[lineStart], lineLen);
            lines[lineIdx][lineLen] = '\0';

            lineIdx++;
            lineStart = i + 1;
        }
    }

    reset_line_iterator();

    return true;
}


/**
 * Frees all allocated memory for lines.
 */
void free_lines(void)
{
    if (lines != NULL) {
        for (size_t i = 0; i < lineCount; i++) {
            free(lines[i]);
        }
        free(lines);
        lines = NULL;
        lineCount = 0;
        currentLineIndex = 0;
    }
}



/**
 * Returns the next line from the parsed lines array.
 * 
 * Returns: pointer to the next line, or NULL if end of file is reached
 */
char* get_next_line(void)
{
    if (lines == NULL || currentLineIndex >= lineCount) {
        return NULL;
    }

    return lines[currentLineIndex++];
}


bool parse_range(const char *line)
{

    for (size_t i = 0; i < strlen(line); i++) {
        if (line[i] == '-') {
            // Split the line into two parts
            char leftPart[32];
            char rightPart[32];
            strncpy(leftPart, line, i);
            leftPart[i] = '\0';
            strcpy(rightPart, &line[i + 1]);

            // Parse both numbers
            arrayBegin[arrayCount] = strtol(leftPart, NULL, 10);
            arrayEnd[arrayCount] = strtol(rightPart, NULL, 10);
            arrayCount++;
            return true;
        }
    }



    return true;
}

bool parse_number(const char *line, unsigned long int *number)
{
    *number = strtol(line, NULL, 10);
    return true;
}


int mode = 1;

int main(void)
{

    bool readSuccess = read_input_file();
    if (readSuccess == false) {
        printf("Failed to read input file.\n");
        return 1;
    }

    bool parseSuccess = parse_lines();
    if (parseSuccess == false) {
        printf("Failed to parse lines from input file.\n");
        free(fileBuffer);
        return 1;
    }

    // Example: iterate through all lines and parse each one
    char *line;

    unsigned long int number;
    
    while ((line = get_next_line()) != NULL) {

        if (line[0] == '\0') {
            mode = 2;
            continue;
        }

        switch(mode) {
            case 1:
                parse_range(line);
                //printf("mode 1 line: %s range: %ld - %ld \n", line, rangeBegin, rangeEnd);
                break;
            case 2:
                parse_number(line, &number);
                //printf("mode 2 line:%s number: %ld \n", line,number);

                break;
            default:
                break;
        }   

        // printf("%s\n", line);
/*
        if (parse_line(line, &number1, &number2)) {

            printf("Direction: %c, Number: %ld, Dial Position: %ld , Zero Count: %d\n", direction, number, dialPosition, zeroCount);
        } else {
            printf("Failed to parse line: %s\n", line);
        }
*/
   }

    printf("Count: %d\n", arrayCount);

    free_lines();
    free(fileBuffer);

    return 0;
}
