#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>
#include <string.h>
#include <stdlib.h>

int main() {

    char command[200];

    while(1) {

        printf("myshell> ");
        fflush(stdout);

        fgets(command, sizeof(command), stdin);

        // Remove newline
        command[strcspn(command, "\n")] = 0;

        // Ignore empty command
        if(strlen(command) == 0) {
            continue;
        }

        // Exit shell
        if(strcmp(command, "exit") == 0) {
            break;
        }

        // Built-in cd
        if(strncmp(command, "cd ", 3) == 0) {

            char *path = command + 3;

            if(chdir(path) != 0) {
                printf("Directory not found\n");
            }

            continue;
        }

        // Background process check
        int background = 0;

        if(command[strlen(command) - 1] == '&') {

            background = 1;

            command[strlen(command) - 1] = '\0';

            // Remove extra space
            if(command[strlen(command) - 1] == ' ') {
                command[strlen(command) - 1] = '\0';
            }
        }

        // PIPE IMPLEMENTATION
        char *pipe_pos = strchr(command, '|');

        if(pipe_pos != NULL) {

            char *left_command = strtok(command, "|");
            char *right_command = strtok(NULL, "|");

            if(right_command == NULL) {
                printf("Invalid pipe command\n");
                continue;
            }

            // Remove leading spaces
            while(*right_command == ' ') {
                right_command++;
            }

            char *left_args[10];
            char *right_args[10];

            // Parse left command
            int i = 0;

            char *token = strtok(left_command, " ");

            while(token != NULL && i < 9) {

                left_args[i++] = token;
                token = strtok(NULL, " ");
            }

            left_args[i] = NULL;

            // Parse right command
            i = 0;

            token = strtok(right_command, " ");

            while(token != NULL && i < 9) {

                right_args[i++] = token;
                token = strtok(NULL, " ");
            }

            right_args[i] = NULL;

            int fd[2];

            if(pipe(fd) < 0) {
                printf("Pipe failed\n");
                continue;
            }

            pid_t pid1 = fork();

            if(pid1 == 0) {

                // First child writes to pipe
                close(fd[0]);

                dup2(fd[1], STDOUT_FILENO);

                close(fd[1]);

                execvp(left_args[0], left_args);

                printf("Command not found\n");

                exit(1);
            }

            pid_t pid2 = fork();

            if(pid2 == 0) {

                // Second child reads from pipe
                close(fd[1]);

                dup2(fd[0], STDIN_FILENO);

                close(fd[0]);

                execvp(right_args[0], right_args);

                printf("Command not found\n");

                exit(1);
            }

            // Parent closes pipe
            close(fd[0]);
            close(fd[1]);

            wait(NULL);
            wait(NULL);

        } else {

            // NORMAL COMMAND EXECUTION

            char *args[10];

            int i = 0;

            char *token = strtok(command, " ");

            while(token != NULL && i < 9) {

                args[i++] = token;

                token = strtok(NULL, " ");
            }

            args[i] = NULL;

            pid_t pid = fork();

            if(pid < 0) {

                printf("Fork failed\n");

            } else if(pid == 0) {

                execvp(args[0], args);

                printf("Command not found\n");

                exit(1);

            } else {

                if(background == 0) {
                    wait(NULL);
                }
            }
        }
    }

    return 0;
}