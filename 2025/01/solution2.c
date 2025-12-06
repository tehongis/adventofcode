#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

/**
 * Reads the contents of "input.txt" into an allocated memory buffer.
 * The caller is responsible for freeing the returned buffer.
 *
 * Returns:
 *   - A pointer to the allocated buffer containing the file contents on success
 *   - NULL on failure (file not found, memory allocation error, etc.)
 */

long int dialPosition = 50;
int zeroCount = 0;

size_t fileSize = 0;
char *fileBuffer = NULL;
char **lines = NULL;
size_t lineCount = 0;
size_t currentLineIndex = 0;

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



/**
 * Parses a single line into a direction character and a number.
 * Expected format: "L 12345" or "R 98765"
 * 
 * Parameters:
 *   line - the line to parse
 *   direction - pointer to store the direction character ('L' or 'R')
 *   number - pointer to store the parsed number
 * 
 * Returns: true on success, false on parse error
 */
bool parse_line(const char *line, char *direction, long *number)
{
    if (line == NULL || direction == NULL || number == NULL) {
        return false;
    }

    // Parse direction (first character)
    if (line[0] != 'L' && line[0] != 'R') {
        fprintf(stderr, "Invalid direction: %c\n", line[0]);
        return false;
    }
    *direction = line[0];

    // Parse number (skip whitespace and convert the rest)
    char *endptr;
    *number = strtol(&line[1], &endptr, 10);
    
    // Check if conversion was successful
    if (endptr == &line[1]) {
        fprintf(stderr, "No valid number found in line: %s\n", line);
        return false;
    }

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

    dialPosition = 50;

    // Example: iterate through all lines and parse each one
    char *line;
    char direction;
    long number;
    long clippedNumber;
    int fullRotations = 0;
    
    while ((line = get_next_line()) != NULL) {
        if (parse_line(line, &direction, &number)) {

            
            fullRotations = (int) (number / 100);

            //printf("%d : %ld\n",fullRotations, number);

            clippedNumber = number % 100;

            if (direction == 'L') {
                clippedNumber = -clippedNumber;
            }

            if (dialPosition + clippedNumber < 0 ) {
                fullRotations = fullRotations + 1;
            }

            dialPosition = ( dialPosition + clippedNumber + 100 ) % 100;

            zeroCount= zeroCount + fullRotations;
            if (dialPosition == 0) {
                zeroCount= zeroCount + 1;
            }

            printf("Direction: %c, Number: %ld, Clippednumber: %ld, Full fullRotations: %d, Dial Position: %ld , Zero Count: %d\n", direction, number,clippedNumber, fullRotations, dialPosition, zeroCount);
        } else {
            printf("Failed to parse line: %s\n", line);
        }
    }

    // TODO: Process the file content here

    free_lines();
    free(fileBuffer);

    return 0;
}
