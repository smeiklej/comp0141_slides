
#include <stdio.h>
#include <string.h>

int check_auth(char *password) {
    int auth_flag = 0;
    char pass[16];

    strcpy(pass, password);
    if (strcmp(pass, "abc123") == 0)
        auth_flag = 1;

    return auth_flag;
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Need to provide a password\n", argv[0]);
    }

    if (check_auth(argv[1]))
        printf("you're logged in\n");
    else
        printf("incorrect password\n");
}
