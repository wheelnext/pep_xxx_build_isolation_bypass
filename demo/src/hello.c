#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *hello(char *name) {
    char *buf = malloc(7+strlen(name));
    sprintf(buf, "hello %s!", name);
    return buf;
}