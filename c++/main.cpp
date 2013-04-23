//
// main.cpp - template program
//
// Copyright 2013 sel
//

#include <cstdio>

int main(int argc, char** argv) {
#ifdef DEBUG
    printf("(debug) ");
#endif

    for (int i = 0; i < argc; i++) {
        printf("%s ", argv[i]);
    }

    printf("\n");

    return 0;
}
